from math import log
import math
from sys import argv
from random import uniform
from numpy import random
from matplotlib import pyplot as plt

def genSample(w,W):
    u = uniform(0,1)
    s=0
    i=0
    while(s<=W*u):
        s+=w[i]
        i+=1
    return i

n=int(argv[1])
N = 1000
summ = 0
w=[]
error = []
k=0
Mn = 0
Gn = 0
for i in range(1,N+1):
    k+= math.pow(i,1.2)
    Gn+=i*math.log(i)

for i in range(1,N+1):
    w.append(math.pow(i,1.2)/k)

W=sum(w)

for i in range(1,n+1):
    y = genSample(w,W)#(N,w)
    Mn = y*math.log(y)*k/math.pow(y,1.2)
    #gn = i*math.log(i)
    error.append(abs(Mn/n - Gn)/Gn)

print(Mn/n)
plt.loglog(error)
plt.axhline(1,0,1000000,color='red')
plt.grid(True,which="both",ls="-")
plt.savefig('lista3-q5-1.png')
plt.ylim(0,1)
plt.show()
