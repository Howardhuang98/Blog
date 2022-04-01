#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   gym初识.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2022/3/29 20:28  
------------      
"""
import time

import gym

env = gym.make('CartPole-v1')
state = env.reset()
for t in range(10000):
    env.render()
    action = env.action_space.sample()
    state, reward, done, info = env.step(action)

env.close()
