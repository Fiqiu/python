# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 22:14:51 2018

@author: GJP
"""
import random
import matplotlib.pyplot as plt
def queue(lambd,rho,simulation_time):
    customers=[]
    t=0
    service=0
    mu=lambd/rho
    waits=[]
    als=[]
    while t<simulation_time:
        if len(customers)==0:
            arrival_time=random.expovariate(lambd)
            service_start_time=arrival_time
            arrival=1
        else:
            
            arrival_time+=random.expovariate(lambd)
            service_start_time=max(arrival_time,customers[-1][-1])
            arrival+=1
            service+=1
        service_time=random.expovariate(mu)
        service_end_time=service_start_time+service_time
        wait=service_start_time-arrival_time
        total=wait+service_time
        customers.append((arrival_time,service_end_time))
        waits.append(wait)
        als.append(total)
        t=arrival_time
    mean_wait=sum(waits)/len(waits)
    mean_time=sum(als)/len(als)
    jobs=2*mean_time
    return (mean_wait,mean_time,jobs)
a=[]
for i in range(1000,400000,3000):
    a.append(queue(2,1,i)[1])
plt.plot(list(range(133)),a)
plt.show()
