from matplotlib import pyplot as plt
import math
from math import pi, sqrt, exp
from sys import argv
from random import uniform

const = sqrt(2*pi)

def genSample(w,W):
    u = uniform(0,1)
    s=0
    i=0
    while(s<=W*u):
        s+=w[i]
        i+=1
    return i

def norm(x):
    return (1/const)*exp(-math.pow(x,2)/2)

def importance(x,b,k):
    return math.exp(x/b)/k

n = int(argv[1])
a = int(argv[2])
b = int(argv[3])
integ = []
impor = []
Mn = 0
counter = 0
k = 0
w=[]
squareArea = (b-a)*(norm(a))

for i in range(a,b+1):
    k += math.exp(i/b)

for i in range(a,b+1):
    w.append(math.exp(i/b)/k)

W = sum(w)

for i in range(1,n+1):
    x_i = uniform(a,b)
    y_i = uniform(0,norm(a))

    if y_i <= norm(x_i): counter+=1
    integ.append(counter*squareArea/i)
    w_i = genSample(w,W)
    Mn = norm(w_i)/importance(w_i,b,k) 
    impor.append(Mn/i)


print(counter*squareArea/n)
plt.plot(impor,color='blue', label='importance sampling')
plt.plot(integ,color='red', label='integration method')
plt.show()
