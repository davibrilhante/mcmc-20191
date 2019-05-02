from random import uniform
from sys import argv
import math
from matplotlib import pyplot as plt

alpha=[]
n=int(argv[1])
x_0 = int(argv[2])
for i in range(int(argv[3])):
    alpha.append(float(argv[i+4]))
for A in alpha:
    dist=[]
    for i in range(1,n+1):
        u = uniform(0,1)
        x_i = x_0/math.pow(u,1/A)
        dist.append(x_i)

    plt.hist(dist, bins=1000, histtype='step',label='$\\alpha$ ='+str(A))
plt.grid(True,which="both",ls="-")
plt.xlim(0,10)
plt.legend(loc=0)
plt.show()
