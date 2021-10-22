#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   写一个神经网络.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2021/10/19 16:18  
------------      
"""
import os
import torch
from torch import nn, tensor
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
        )

    def forward(self, x:tensor):
        print(x.size())
        x = self.flatten(x)
        print(x.size())
        logits = self.linear_relu_stack(x)
        print(logits.size())
        return logits


if __name__ == '__main__':
    model = NeuralNetwork()
    print(model)
    X = torch.rand(1,28,28)
    l = model(X)
    print(l)