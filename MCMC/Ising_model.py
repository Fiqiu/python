# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 01:24:27 2018

@author: GJP
"""

import random
import math
import numpy as np
import matplotlib
betalist=[-1.5,-1,0,0.2,0.4,0.441,0.5,1,2,10]
trials=10**5
for z in range(len(betalist)):
    beta=betalist[z]
    g=60
    grid=np.random.choice([-1,1],(g+2,g+2))
    grid[0,:]=0
    grid[g+1,:]=0
    grid[:,0]=0
    grid[:,g+1]=0
    rc=list(range(g+1))
    rc.pop(0)
    for m in range(trials):
        i=random.randint(1,g)
        j=random.randint(1,g)
        deg=grid[i,j+1]+grid[i,j-1]+grid[i-1,j]+grid[i+1,j]
        p=1/(1+pow(math.e,-beta*2*deg))
        if random.uniform(0,1)<p:
            grid[i,j]=1
        else:
            grid[i,j]=-1
    final=grid[1:g,1:g]
print(grid)
