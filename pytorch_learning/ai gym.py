#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   ai gym.py    
@Contact :   huanghoward@foxmail.com
@Modify Time :    2021/9/23 10:44  
------------      
"""
import gym
env = gym.make('CartPole-v1')
for i_episode in range(1000):
    observation = env.reset()
    for t in range(1000):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()