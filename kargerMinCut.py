# The code is slow for the last test files and hence need to be improved
import random, copy
from datetime import datetime
#==========================================================
def graphlist(edges):
    components = []
    for v1, v2 in edges:
        check1=True; check2=True
        for component in components:
            if v1 == component[0] :
                check1=False
            if v2 == component[0] :
                check2=False
        if check1:
            components.append([v1])
        if check2:
            components.append([v2])
        for component in components:
            if v1 == component[0] :
                component.append(v2)
            if v2 == component[0] :
                component.append(v1)
    return components
#==========================================================
def kargerMinCut(G):
    MinCut = []
    while len(G) > 2:
        v1 = random.choice(list(G.keys()))
        v2 = random.choice(list(G[v1]))
        # Contract
        G[v1].extend(G[v2])
        for x in G[v2]:
            G[x].remove(v2)
            G[x].append(v1) 
        # Remove self-loop
        while v1 in G[v1]:
            G[v1].remove(v1)
        del G[v2]
    for key in G.keys():
        MinCut.append(len(G[key]))
    return MinCut[0]
#==========================================================
def run(file):
    data = open(file,"r")
    pairs = []
    for line in data:
        lst = [int(s) for s in line.split()]
        pairs.append((lst[0], lst[1]))  
    data = graphlist(pairs)
    G = {}
    for i in range(len(data)):
        lst = data[i]
        G[lst[0]] = lst[1:]  
    i=0; count = 10000       
    while i < 1000:
        data = copy.deepcopy(G)
        MinCut = kargerMinCut(data)
        if MinCut < count:
            count = MinCut
        i = i + 1
    print(count)