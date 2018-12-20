# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 01:06:45 2018

@author: GJP
"""

import random
import numpy as np
import matplotlib.pyplot as plt
(p,n)=0.5,800
pset=[]
nset=[]
def gibbs(p,n,x,lambd,a,b):
    p=random.betavariate(x+a,n-x+b)
    y=np.random.poisson(lambd*(1-p))
    n=x+y
    return(p,n)
means=[]
variances=[]
for i in range(10**3):
    (p,n)=gibbs(p,n,7,10,1,1)
    pset.append(p)
    nset.append(n)
    if int(i)==i:
        means.append(np.mean(np.array(nset)))
        variances.append(np.std(np.array(nset)))
#plt.hist(nset,20)
plt.plot(range(1000),variances)
plt.show()