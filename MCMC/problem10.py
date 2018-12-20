# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 02:21:23 2018

@author: GJP
"""
import random
coloring=['red','black','white','yellow','blue','green','gray']
nodes=10
graphs=set()
graph=[]
graphs2=[]
edges=[{1,2},{2,3},{3,4},{4,5},{5,7},{3,7},{2,7},{7,10}\
       ,{5,8},{5,6},{8,9},{7,8}]
#edges=[{1,2},{2,3},{3,4},{4,5},{1,5},{1,7},{2,8},{3,9},{4,10},{5,6},\
#       {7,10},{6,9},{6,8},{7,9},{8,10}]
Trees=[{1,2},{2,3},{3,4},{4,5},{5,6},{5,8},{8,7}]
treenodes=8
def qualifygraph(graph):
    No=[]
    for edge in Trees:
        edge=list(edge)
        if graph[edge[0]-1]==graph[edge[1]-1]:
            No.append(1)
            break
    if No==[]:
        return graph
    else:
        return []
for i in range(treenodes):
        graph.append(coloring[random.randint(0,2)])
'''
def generatelegal():
    graph=[]
    for i in range(nodes):
        graph.append(coloring[random.randint(0,2)])
    for edge in edges:
        edge=list(edge)
        if graph[edge[0]-1]==graph[edge[1]-1]:
            nod=edge[0]
            connected=[]
            for edge in edges:
                if nod in edge:
                    connected.append(edge)
            allconnected=set()
            for edge in connected:
                allconnected=allconnected|edge
            allconnected=allconnected-{nod}
            nopainting=set()
            for nod in allconnected:
                nopainting.add(graph[nod-1])
                repainting=['red','black','white','yellow','blue','green']
            for color in nopainting:
                repainting.remove(color)
            if repainting == []:
                return graph 
            else:
                graph[nod-1]=repainting[random.randint(0,len(repainting)-1)]
                return graph
    return graph
'''
'''
while len(graphs2)<5000:
        graphs2.append(generatelegal())
'''
def gibbs(node,graph):
    connected=[]
    for edge in Trees:
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
    '''painted6=set()
    for nod in {2,3,4,5,8}:
        painted6.add(graph[nod-1])
    ablepaint6=set(repainting)-painted6
    '''
    if repainting == []:
        return graph
    else:
        graph[node-1]=repainting[random.randint(0,len(repainting)-1)]
        return graph
    
for i in range(10**8):
    graph=gibbs(random.randint(1,8),graph)
    graphs.add(tuple(qualifygraph(graph)))
graphs=graphs-{()}
kind=0
for graph in graphs:
    connected=set()
    connected=connected|set(graph[1:4])
    connected.add(graph[7])
    ablepaint={'red','black','white','yellow','blue','green','gray'}-connected
    kind+=len(ablepaint)*6
print(kind)