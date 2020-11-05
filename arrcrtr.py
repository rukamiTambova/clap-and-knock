import numpy as np
d = [12, 22,36,19,122]
def func(data):
    aparr = []
    for item in d:
        softarray = []
        for k in range(len(str(item))):
            softarray.append(int(str(item)[k:k+1]))
        aparr.append(softarray)
    nr = np.array(aparr, dtype = object)
    
    for item in nr:
        for k in range(len(item)-1):
            item[k+1]=item[k+1]+item[k]
    return(nr)
            
print(func(d))
def max_lenarr(arr):
    x = []
    for i in arr:
        x.append(len(i))
    return x
print(max_lenarr(func(d)))
print(np.amax(max_lenarr(func(d))))

def i_massiv(nr):
    soft = np.zeros([np.amax(max_lenarr(nr))*9+1])
    general = []
    general.append(soft)
    for i in range(len(soft)):
        soft[i]=i
    #a_massiv = [0,0,0,0,0,0,0,0,0,0]
    #return general
    for k in range(np.amax(max_lenarr(nr))):
        a_massiv = np.zeros([len(np.amax(nr, axis =0))*9+1])
        for i in range(len(soft)):
            for item in nr:
                if len(item)>k:
                    if item[k]==i:
                        a_massiv[i]+=1
                
        general.append(a_massiv)
    
    return general
        
            

#print(i_massiv(np.array(func(d))))
print(func(d))
print(i_massiv(func(d)))    
