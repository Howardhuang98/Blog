#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   model.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/4/7 20:00  
------------      
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
import math

from torch.autograd import Variable
from utils import my_softmax, get_offdiag_indices, gumbel_softmax, preprocess_adj, preprocess_adj_new, preprocess_adj_new1, gauss_sample_z, my_normalize

_EPS = 1e-10


class MLPEncoder(nn.Module):
    """MLP encoder module."""
    def __init__(self, n_in, n_xdims, n_hid, n_out, adj_A, batch_size, do_prob=0., factor=True, tol = 0.1):
        super(MLPEncoder, self).__init__()

        self.adj_A = nn.Parameter(Variable(torch.from_numpy(adj_A).double(), requires_grad=True))
        self.factor = factor

        self.Wa = nn.Parameter(torch.zeros(n_out), requires_grad=True)
        self.fc1 = nn.Linear(n_xdims, n_hid, bias = True)
        self.fc2 = nn.Linear(n_hid, n_out, bias = True)
        self.dropout_prob = do_prob
        self.batch_size = batch_size
        self.z = nn.Parameter(torch.tensor(tol))
        self.z_positive = nn.Parameter(torch.ones_like(torch.from_numpy(adj_A)).double())
        self.init_weights()

    def init_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Linear):
                nn.init.xavier_normal_(m.weight.data)
            elif isinstance(m, nn.BatchNorm1d):
                m.weight.data.fill_(1)
                m.bias.data.zero_()


    def forward(self, inputs, rel_rec, rel_send):

        if torch.sum(self.adj_A != self.adj_A):
            print('nan error \n')

        # to amplify the value of A and accelerate convergence.
        adj_A1 = torch.sinh(3.*self.adj_A)

        # adj_Aforz = I-A^T
        adj_Aforz = preprocess_adj_new(adj_A1)

        adj_A = torch.eye(adj_A1.size()[0]).double()
        H1 = F.relu((self.fc1(inputs)))
        x = (self.fc2(H1))
        logits = torch.matmul(adj_Aforz, x+self.Wa) -self.Wa

        return x, logits, adj_A1, adj_A, self.z, self.z_positive, self.adj_A, self.Wa

class MLPDEncoder(nn.Module):
    def __init__(self, n_in, n_hid, n_out, adj_A, batch_size, do_prob=0., factor=True, tol = 0.1):
        super(MLPDEncoder, self).__init__()

        self.adj_A = nn.Parameter(Variable(torch.from_numpy(adj_A).double(), requires_grad=True))
        self.factor = factor

        self.Wa = nn.Parameter(torch.tensor(0.0), requires_grad=True)
        self.fc1 = nn.Linear(n_hid, n_hid, bias = True)
        self.fc2 = nn.Linear(n_hid, n_out, bias = True)

        n_var = adj_A.shape[0]
        self.embed = nn.Embedding(n_out, n_hid)
        self.dropout_prob = do_prob
        self.alpha =  nn.Parameter(Variable(torch.div(torch.ones(n_var, n_out),n_out)).double(), requires_grad = True)
        self.batch_size = batch_size
        self.z = nn.Parameter(torch.tensor(tol))
        self.z_positive = nn.Parameter(torch.ones_like(torch.from_numpy(adj_A)).double())

        self.init_weights()

    def init_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Linear):
                nn.init.xavier_normal_(m.weight.data)
            elif isinstance(m, nn.BatchNorm1d):
                m.weight.data.fill_(1)
                m.bias.data.zero_()

    def forward(self, inputs, rel_rec, rel_send):

        if torch.sum(self.adj_A != self.adj_A):
            print('nan error \n')

        adj_A1 = torch.sinh(3.*self.adj_A)

        adj_Aforz = preprocess_adj_new(adj_A1)
        adj_A = torch.eye(adj_A1.size()[0]).double()

        bninput = self.embed(inputs.long().view(-1, inputs.size(2)))
        bninput = bninput.view(*inputs.size(),-1).squeeze()
        H1 = F.relu((self.fc1(bninput)))
        x = (self.fc2(H1))


        logits = torch.matmul(adj_Aforz, x+self.Wa) -self.Wa

        prob = my_softmax(logits, -1)
        alpha = my_softmax(self.alpha, -1)

        return x, prob, adj_A1, adj_A, self.z, self.z_positive, self.adj_A, self.Wa, alpha


class SEMEncoder(nn.Module):
    """SEM encoder module."""
    def __init__(self, n_in, n_hid, n_out, adj_A, batch_size, do_prob=0., factor=True, tol = 0.1):
        super(SEMEncoder, self).__init__()

        self.factor = factor
        self.adj_A = nn.Parameter(Variable(torch.from_numpy(adj_A).double(), requires_grad = True))
        self.dropout_prob = do_prob
        self.batch_size = batch_size

    def init_weights(self):
        nn.init.xavier_normal(self.adj_A.data)

    def forward(self, inputs, rel_rec, rel_send):

        if torch.sum(self.adj_A != self.adj_A):
            print('nan error \n')

        adj_A1 = torch.sinh(3.*self.adj_A)

        # adj_A = I-A^T, adj_A_inv = (I-A^T)^(-1)
        adj_A = preprocess_adj_new((adj_A1))
        adj_A_inv = preprocess_adj_new1((adj_A1))

        meanF = torch.matmul(adj_A_inv, torch.mean(torch.matmul(adj_A, inputs), 0))
        logits = torch.matmul(adj_A, inputs-meanF)

        return inputs-meanF, logits, adj_A1, adj_A, self.z, self.z_positive, self.adj_A
