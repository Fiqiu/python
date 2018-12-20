# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 22:21:16 2018

@author: GJP
"""
import  matplotlib.pyplot as plt
import random
def good_sequence(init,n):
    length=len(init)
    total=0
    new=[2]+init+[2]
    for i in range(n):
        index=random.randint(1,length)
        if new[index] == 1:
            new[index]=0
            total+=sum(new)
        else:
            if new[index-1]==1 or new[index+1]==1:
                total+=sum(new)
            else:
                new[index]=1
                total+=sum(new)
    return total/n-4
init=[0]*88
num=[0,1]

k=[]
'''
for i in range(20):
    k.append(good_sequence(init,1000000))
    print(k)
print(sum(k)/20)
'''

for i in range(50):
    for i in range(1000,100000,50):
        num.append(good_sequence(init,i))
        try:
            if abs(num[-1]-num[-2])<0.1 and abs(num[-1]-24.47) <0.1:
                k.append(i)
                break
        finally:
            pass
print(sum(k)/50)
print(k)
'''
for i in range(1,100000,10):
    k.append(good_sequence(init,i))
'''
#print(num)
