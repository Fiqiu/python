# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 01:19:14 2018

@author: GJP
"""

import numpy as np
import matplotlib.pyplot as plt
(p,n,x)=0.5,2,1
seta=[]
setb=[]
def gibbs(p,n,x):
    x=np.random.binomial(n,p)
    p=np.random.beta(x+1,n-x+1)
    n=np.random.poisson(4*(1-p))+x
    return (p,n,x)
means=[]
variances=[]
for i in range(2000):
    p,n,x=gibbs(p,n,x)
    seta.append((p,n,x))
    setb.append(n)
    if int(i)==i:
        means.append(np.mean(np.array(setb)))
        variances.append(np.std(np.array(setb)))
#plt.hist(setb,10)
plt.plot(range(2000),variances)
plt.show()