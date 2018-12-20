# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 20:29:42 2018

@author: GJP
"""

import random
import math
import matplotlib.pyplot as plt
import numpy as np
theta=[]
def randf(p):
    rand=random.uniform(0,1)
    if rand<=p:
        return 0
    else:
        return 1
def normal(s,a,b):
    t=random.uniform(s-1,s+1)
    if randf(pow(math.e,-(t**2-s**2)/2))==0:
        return t
    else:
        return s
s=random.uniform(-1,1)
variances=[]
means=[]
for i in range(10**4):
    s=normal(s,5,5)
    theta.append(s)
    if int(i/10)==i/10:
        means.append(np.mean(np.array(theta)))
        variances.append(np.std(np.array(theta)))
plt.plot(range(1000),means)
#plt.hist(theta,30)
plt.show()
    