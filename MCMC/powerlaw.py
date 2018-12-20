# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 01:33:23 2018

@author: GJP
"""

import random
def randf(p):
    rand=random.uniform(0,1)
    if rand<=p:
        return 0
    else:
        return 1
trials=pow(10,6)
def powerlaw(trials,init):
    simlist=[0]*trials
    simlist[0]=init
    for i in range(1,trials):
        if simlist[i-1]==1:
            first=random.randint(0,1)
            if first==0:
                simlist[i]=1
            else:
                p=pow((1/2),(3/2))
                if  randf(p)==0:
                    simlist[i]=2
                else:
                    simlist[i]=1
        else:
            other=random.randint(0,1)
            if other==0:
                simlist[i]=simlist[i-1]-1
            else:
                p=pow((simlist[i-1]/(simlist[i-1]+1)),(3/2))
                if randf(p)==0:
                    simlist[i]=1+simlist[i-1]
                else:
                    simlist[i]=simlist[i-1]
    return simlist

'''
num=[500*x for x in range(1,200)]
k=range(1,500,5)
p=[]
for i in range(99):
    for j in range(1,2):
        p.append(powerlaw((num[i]),1).count(j)/num[i])
print(p)
'''    
num=[]
for i in range(1,9):
    num.append(powerlaw(100000,1).count(i)/trials)
print(num)
