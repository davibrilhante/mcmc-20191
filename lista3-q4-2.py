from math import exp, pi, sqrt, log
from sys import argv
from random import uniform, choice
from matplotlib import pyplot as plt

const = 1/(sqrt(2*pi))

def exponential(Lambda):
    u = uniform(0,1)
    x_i = -1*log(1-u)/Lambda
    return x_i

def distExp(x,Lambda):
    return Lambda*(exp(-Lambda*x))

def distNorm(x,mu,sigma):
    return const*exp(-(x**2)/2)

n=int(argv[1])
expo = []
norm = []
#samples = [-20+40*(i/1000) for i in range(1000)] 
for i in range(n):
    multi = choice([-1,1])
    x_i = exponential(1)
    u = uniform(0,distExp(x_i,1))
    expo.append(x_i)
    if u < distNorm(multi*x_i,1,0):
        norm.append(multi*x_i)

#plt.plot(expo, label='exponential')
plt.hist(expo, bins=1000, label='exponential', histtype='step', density=True)
plt.hist(norm, bins=1000, label='normal', histtype='step', density=True)
plt.legend()
plt.show()
