# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 02:52:42 2018

@author: GJP
"""

import random
def randf(p):
    rand=random.uniform(0,1)
    if rand<=p:
        return 0
    else:
        return 1
def zipf(a,m):
    trials=pow(10,6)
    simlist=[0]*trials
    simlist[0]=2
    for i in range(1,trials):
        if simlist[i-1]==1:
            first=random.randint(0,1)
            if first==0:
                simlist[i]=1
            else:
                p=pow((1/2),(a))
                if  randf(p)==0:
                    simlist[i]=2
                else:
                    simlist[i]=1
        else:
            other=random.randint(0,1)
            if other==0:
                simlist[i]=simlist[i-1]-1
            else:
                p=pow((simlist[i-1]/(simlist[i-1]+1)),(a))
                if randf(p)==0:
                    simlist[i]=1+simlist[i-1]
                else:
                    simlist[i]=simlist[i-1]
    return simlist
num=[]
trials=pow(10,6)
for i in [0.1*x for x in range(1,20)]:
    num.append(zipf(i,1).count(1)/trials)
'''
for i in range(1,9):
    num.append(zipf(0.5,2).count(i)/trials)
'''
print(num)