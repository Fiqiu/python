# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 23:32:53 2018

@author: GJP
"""

import random
import numpy as np
import matplotlib.pyplot as plt
(x,y)=(0,0)
points1=[]
points2=[]
def gibbs(x,y,pho):
    x=random.gauss(pho*y,(1-pho**2)**(1/2))
    y=random.gauss(pho*x,(1-pho**2)**(1/2))
    return (x,y)
means=[]
variances=[]
xa=[]
ya=[]
for i in range(10**3):
    (x,y)=gibbs(x,y,0.6)
    (x,y)=gibbs(x,y,-0.6)
    xa.append(x)
    ya.append(y)
    if int(i)==i:
        means.append(np.mean(np.array(ya)))
        variances.append(np.std(np.array(ya)))
plt.plot(range(1000),variances)
plt.show()