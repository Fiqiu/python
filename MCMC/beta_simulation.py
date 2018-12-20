# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 20:17:40 2018

@author: GJP
"""
import random
import matplotlib.pyplot as plt
import numpy as np
theta=[]
def randf(p):
    rand=random.uniform(0,1)
    if rand<=p:
        return 0
    else:
        return 1
def beta(w,a,b):
    u=random.uniform(0,1)
    if randf(u**(a-1)*(1-u)**(b-1)/(w**(a-1)*(1-w)**(b-1)))==0:
        return u
    else:
        return w
w=random.uniform(0,1)
variances=[]
means=[]
for i in range(10**4):
    w=beta(w,5,5)
    theta.append(w)
    if int(i/10)==i/10:
        means.append(np.mean(np.array(theta)))
        variances.append(np.std(np.array(theta)))
plt.plot(range(1000),variances)
plt.show()
    