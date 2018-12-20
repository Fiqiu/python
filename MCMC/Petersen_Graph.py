# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 22:50:46 2018

@author: GJP
"""
import random
coloring=['red','black','white','yellow','blue','green','gray']
nodes=10
graphs=set()
graph=[]
for i in range(nodes):
    graph.append(coloring[random.randint(0,2)])
edges=[{1,2},{2,3},{3,4},{4,5},{1,5},{1,7},{2,8},{3,9},{4,10},{5,6},\
       {7,10},{6,9},{6,8},{7,9},{8,10}]
def gibbs(node,graph):
    connected=[]
    for edge in edges:
        if node in edge:
            connected.append(edge)
    allconnected=set()
    for edge in connected:
        allconnected=allconnected|edge
    allconnected=allconnected-{node}
    nopainting=set()
    for nod in allconnected:
        nopainting.add(graph[nod-1])
    repainting=['red','black','white','yellow','blue','green','gray']
    for color in nopainting:
        repainting.remove(color)
    if repainting == []:
        return graph
    else:
        graph[node-1]=repainting[random.randint(0,len(repainting)-1)]
        return graph
def qualifygraph(graph):
    No=[]
    for edge in edges:
        edge=list(edge)
        if graph[edge[0]-1]==graph[edge[1]-1]:
            No.append(1)
            break
    if No==[]:
        return graph
    else:
        return []
for i in range(10**3):
    for j in range(10**7):
        graph=gibbs(random.randint(1,10),graph)
        graphs.add(tuple(qualifygraph(graph)))
    print(len(graphs))
graphs=graphs-{()}
print(len(graphs))