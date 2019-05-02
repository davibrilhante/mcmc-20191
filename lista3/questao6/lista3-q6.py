from random import uniform
from sys import argv
import math
from matplotlib import pyplot as plt
from matplotlib import rcParams as rc

rc['agg.path.chunksize'] = 10000

alpha = float(argv[1])
numA = float(argv[2])
numB = float(argv[3])
runs = int(argv[4])

sample = [numA + ((numB-numA)*i/1000) for i in range(1001)]
gradient = [math.pow(i,alpha) for i in sample]

Min = min(gradient)
Max = max(gradient)
inside = [[],[]]
outside = [[],[]]
error = []
counter = 0
functionG = (1/(alpha+1))*(math.pow(numB,alpha+1)-math.pow(numA,alpha+1))
squareArea = (numB-numA)*(Max-Min)
print("g()",functionG)
for n in range(runs):
    x = uniform(numA,numB)
    y = uniform(Min,Max)

    if y <= math.pow(x,alpha):
        counter+=1
        inside[0].append(x)
        inside[1].append(y)
    else:
        outside[0].append(x)
        outside[1].append(y)
    error.append(abs((counter*squareArea/(n+1) - functionG))/functionG)

Mn = counter/runs
print(Mn)
print(Mn*squareArea)

if(argv[5]) == 'f':
    plt.plot(inside[0],inside[1],marker='.',color='blue',label='area below f(x)')
    plt.plot(outside[0],outside[1],marker='.',color='red',label='area over f(x)')
    plt.legend()

elif argv[5]=='e':
    plt.loglog(error)
    plt.title('$\\alpha=$'+argv[1]+', $a$='+argv[2]+', $b$='+argv[3])
    plt.grid(True,which="both",ls="-")
    plt.savefig('lista3-q6-'+argv[1]+'-'+argv[2]+'-'+argv[3]+'.png')

plt.show()
