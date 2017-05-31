# Dictionary 

from numpy import random

def Select(d):
    
    k = []
    for i in d.keys():
        k.append(i)
        
    l = len(k)
    ri = random.random()
    
    s = 0
    for i in d.keys():
        s += d[i]
        
    for i in d.keys():
        d[i] = d[i]/s
    
    cumsum = 0
    dlower = {}
    dupper = {}
    for i in range(len(k)):
        dlower[k[i]] = cumsum
        dupper[k[i]] = cumsum + d[k[i]]
        cumsum += d[k[i]]
        
    for i in dlower.keys():
        if ri >= dlower[i] and ri < dupper[i]:
            return i 

Select(d)
