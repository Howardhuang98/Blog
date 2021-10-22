#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   储存模型.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2021/10/19 17:01  
------------      
"""
import torch
import torch.onnx as onnx
import torchvision.models as models

# 下载模型
model = models.vgg16(pretrained=True)
# 储存权重
torch.save(model.state_dict(), 'model_weights.pth')

# 加载模型
model = models.vgg16() # we do not specify pretrained=True, i.e. do not load default weights
model.load_state_dict(torch.load('model_weights.pth'))
model.eval()
# be sure to call model.eval() method before inferencing to set the dropout and batch normalization layers to evaluation mode. Failing to do this will yield inconsistent inference results.

torch.save(model, 'model.pth')
model = torch.load('model.pth')