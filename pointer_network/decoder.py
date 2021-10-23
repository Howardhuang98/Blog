#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   decoder.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2021/10/22 21:16  
------------      
"""

import torch

class Decoder:

    def __init__(self,encoder_output, config):
        self.encoder_output = encoder_output
        self.h = torch.transpose(encoder_output,)


