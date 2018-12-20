# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 19:18:16 2018

@author: GJP
"""
import random
import math
import matplotlib.pyplot as plt
import numpy as np
theta=[]
d=[0.01,0,1,0.5,1,5,10,15,20,50,80,100]
def randf(p):
    rand=random.uniform(0,1)
    if rand<=p:
        return 0
    else:
        return 1
def stdndistribution(x,y,d,miu,sigma,t):
    xt=x+random.gauss(0,80)
    if randf(pow(math.e,-(y-xt)**2/(2*sigma**2)-(xt-miu)**2/(2*t**2))/\
             pow(math.e,-(y-x)**2/(2*sigma**2)-(x-miu)**2/(2*t**2)))==0:
        return xt
    else:
        return x
x=2
for i in range(10**6):
    x=stdndistribution(x,3,0.1,0,1,2)
    theta.append(x)
plt.hist(theta,30)
plt.show()
sum(theta)/len(theta)
print(np.mean(np.array(theta)))
print(np.std(np.array(theta)))
