# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 18:38:08 2018

@author: GJP
"""
import random
chain=[(1,13),(2,14),(3,15),(4,16),(5,17),(6,18),(7,19),(8,20),\
       (9,21),(10,22),(11,23),(12,24),(1,9),(1,5),(2,6),(2,10),\
       (3,7),(3,11),(4,8),(4,12),(5,9),(6,10),(7,11),(8,12),(13,14),(14,15)\
       ,(15,16),(16,17),(17,18),(18,19),(19,20),(20,21),(21,22),(22,23),(23,24),(13,24)]
painted=set()
stop=[]
graphs=set()
al={(1, 3, 8, 10, 14, 17, 19, 21, 23), (4, 6, 9, 11, 13, 15, 17, 20, 22, 24), (1, 2, 3, 12, 17, 20, 23), (1, 4, 6, 11, 15, 17, 19, 21, 24), (2, 5, 8, 11, 13, 16, 18, 21, 24), (4, 5, 7, 10, 14, 18, 20, 24), (1, 6, 8, 11, 15, 17, 19, 21, 24), (1, 6, 11, 12, 14, 16, 19, 21), (1, 2, 8, 11, 15, 17, 19, 22, 24), (1, 7, 14, 16, 18, 20, 22, 24), (5, 7, 8, 10, 13, 15, 18, 21, 23), (3, 4, 5, 6, 14, 19, 21, 23), (3, 5, 12, 14, 16, 18, 20, 22), (4, 6, 7, 9, 13, 15, 17, 20, 22, 24), (5, 7, 8, 10, 13, 15, 18, 21, 24), (1, 2, 3, 12, 16, 18, 20, 22), (5, 6, 8, 11, 14, 16, 19, 21, 24), (5, 6, 11, 13, 16, 20, 22, 24), (1, 6, 8, 11, 14, 16, 19, 21, 24), (5, 6, 7, 8, 13, 16, 21, 23), (2, 4, 9, 11, 13, 15, 18, 20, 22, 24), (4, 7, 9, 10, 14, 18, 20, 23), (2, 8, 9, 11, 13, 15, 17, 19, 22, 24), (5, 6, 8, 11, 14, 16, 19, 22, 24), (1, 3, 6, 12, 14, 17, 19, 21, 23), (3, 5, 6, 8, 13, 16, 19, 22, 24), (1, 2, 7, 12, 15, 17, 20, 23), (2, 3, 8, 9, 13, 16, 19, 22, 24), (6, 9, 11, 12, 14, 16, 19, 22), (3, 5, 10, 12, 13, 16, 19, 21, 23), (6, 7, 8, 9, 13, 15, 17, 22, 24), (1, 4, 7, 10, 14, 18, 21, 23), (10, 12, 13, 15, 17, 19, 21, 23), (4, 5, 6, 7, 14, 20, 22, 24), (9, 10, 12, 13, 15, 17, 19, 23), (3, 5, 10, 12, 14, 16, 19, 21, 23), (3, 4, 6, 9, 14, 17, 20, 23), (5, 11, 12, 14, 16, 18, 20, 22), (2, 4, 5, 7, 13, 15, 18, 20, 23), (4, 5, 7, 10, 13, 15, 18, 21, 23), (5, 7, 10, 12, 13, 15, 18, 21, 23), (1, 10, 11, 12, 14, 16, 19, 21), (3, 6, 8, 13, 17, 19, 21, 24), (1, 6, 7, 12, 14, 16, 21, 23), (5, 7, 8, 10, 14, 16, 18, 21, 23), (1, 2, 8, 11, 15, 17, 19, 21, 24), (5, 6, 11, 12, 13, 16, 19, 22), (4, 7, 9, 10, 13, 15, 18, 20, 24), (8, 10, 11, 13, 15, 17, 19, 21, 24), (1, 3, 4, 10, 14, 17, 19, 21, 23), (3, 4, 9, 10, 13, 18, 20, 23), (4, 5, 7, 10, 14, 18, 20, 23), (1, 10, 11, 12, 14, 17, 20), (8, 10, 13, 15, 17, 19, 21, 23), (2, 7, 12, 13, 15, 17, 21, 23), (2, 3, 5, 12, 13, 16, 19, 21, 23), (1, 6, 11, 14, 16, 20, 22, 24), (4, 5, 6, 7, 13, 15, 20, 23), (2, 4, 5, 7, 13, 15, 18, 21, 23), (3, 6, 9, 12, 14, 16, 19, 22), (3, 5, 6, 8, 14, 16, 19, 21, 24), (1, 4, 7, 10, 15, 18, 20, 23), (2, 9, 11, 12, 13, 15, 17, 19, 22), (2, 8, 11, 13, 15, 17, 19, 21, 24), (3, 4, 5, 6, 13, 19, 21, 24), (1, 2, 7, 12, 15, 18, 21, 23), (2, 3, 4, 5, 13, 19, 22, 24), (1, 3, 6, 8, 14, 17, 19, 21, 24), (1, 2, 7, 12, 16, 18, 20, 22), (1, 3, 8, 10, 14, 16, 18, 21, 23), (4, 7, 9, 10, 13, 15, 18, 20, 23), (4, 6, 7, 9, 14, 17, 20, 22, 24), (5, 6, 11, 12, 14, 16, 19, 21), (1, 8, 10, 11, 14, 17, 19, 21, 24), (1, 3, 6, 8, 14, 17, 19, 21, 23), (2, 3, 5, 12, 13, 16, 18, 20, 23), (5, 7, 10, 12, 14, 16, 18, 21, 23), (3, 6, 8, 9, 14, 16, 19, 22, 24), (3, 4, 6, 9, 13, 17, 20, 22, 24), (7, 9, 10, 12, 14, 16, 18, 20, 23), (3, 5, 6, 12, 14, 16, 19, 21, 23), (6, 8, 9, 11, 13, 15, 17, 19, 22, 24), (3, 5, 6, 8, 13, 16, 19, 21, 23), (7, 8, 9, 10, 13, 15, 18, 24), (2, 4, 9, 13, 15, 17, 19, 23), (3, 6, 9, 12, 14, 16, 20, 23), (2, 4, 7, 9, 13, 15, 17, 20, 22, 24), (1, 2, 4, 7, 15, 18, 20, 22, 24), (1, 4, 7, 10, 14, 18, 21, 24), (1, 6, 11, 12, 14, 17, 19, 21), (2, 5, 11, 12, 13, 15, 18, 20, 22)}
for j in range(100):
    count=0
    painted=set()
    for i in range(1000):
        connected=set()
        rand = random.randint(1,24)
        if rand in painted:
            painted.discard(rand)
        for node  in  chain:
            if rand in node:
                connected=connected|(set(node)-{rand})
        if connected & painted == set():
            painted.add(rand)
        count+=1
        if tuple(painted)in al :
            print(count)
            break
    graphs.add(tuple(painted))
def leng(x):
    return len(x)
print(max(map(len,graphs)))
'''
        stop.append(1)
        print(painted)    
    else:
        stop.append(0)
    try:
        t=stop[-100,-1]
        if t.count(0)==len(t):
            break
    except Exception:
        continue
'''