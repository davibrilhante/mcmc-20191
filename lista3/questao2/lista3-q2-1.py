from random import uniform
from sys import argv
from math import log
from matplotlib import pyplot as plt
counter = 0
Lambda=[]
n=int(argv[1])
for i in range(int(argv[2])):
    Lambda.append(float(argv[i+3]))
for l in Lambda:
    dist=[]
    for i in range(1,n+1):
        u = uniform(0,1)
        x_i = -1*log(1-u)/l
        dist.append(x_i)

    plt.hist(dist, bins=1000, histtype='step',label='$\lambda$ ='+str(l))
plt.grid(True,which="both",ls="-")
plt.legend(loc=0, )
plt.show()
