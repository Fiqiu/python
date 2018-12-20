# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:17:00 2018

@author: GJP
"""

import random
def good_sequence(init,n):
    good=0
    bad=0
    length=len(init)
    new=[2]+init+[2]
    for i in range(n):
        index=random.randint(1,length)
        if new[index] == 1:
            new[index]=0
            good+=1
        else:
            if new[index-1]==1 or new[index+1]==1:
                bad+=1
            else:
                new[index]=1
                good+=1
    return bad/(good+bad)
init=[0]*88
print(good_sequence(init,100000))
