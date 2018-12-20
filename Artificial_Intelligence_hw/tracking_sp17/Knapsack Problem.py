# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 18:35:42 2018

@author: GJP
"""
import random
import math
import matplotlib.pyplot as plt
import numpy as np
gj=[6,3,5,4,6]
wj=[2,2,6,5,4]
m=5
w=10
chain=[0,0,0,0,0]
beta=0.5
def randf(p):
    rand=random.uniform(0,1)
    if rand<=p:
        return 0
    else:
        return 1
def Knapsackproblem(gj,wj,m,w,chain,beta):
    rand=random.randint(1,len(chain))
    chain2=chain.copy()
    chain2[rand-1]=1-chain[rand-1]
    weight=0
    value1=0
    value2=0
    for i in range(len(wj)):
        weight+=wj[i]*chain2[i]
    if weight>w:
        return chain
    elif weight<=w:
        for i in range(len(gj)):
            value1+=gj[i]*chain[i]
            value2+=gj[i]*chain2[i]
        if randf(pow(math.e,beta*(value2-value1)))==0:
            return chain2
        else:
            return chain
chain=Knapsackproblem(gj,wj,m,w,chain,beta)
beta1=[0.0007*x for x in range(500)]
beta2=[0.4+0.0005*x for x in range(1500)]
beta=beta1+beta2
value=0
allchain=[]
variances=[]
for i in range(2000):
    chain=Knapsackproblem(gj,wj,m,w,chain,beta[i])
    value=0
    for j in range(len(gj)):
        value+=gj[j]*chain[j]
        allchain.append(value)
    variances.append(np.std(np.array(allchain)))
plt.plot(list(range(1900)),variances[100:2000])
plt.show()
#print(variances)
