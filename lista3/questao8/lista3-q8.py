from matplotlib import pyplot as plt
import math
from math import pi, sqrt, exp
from sys import argv
from random import uniform

const = sqrt(2*pi)

def genSample(weightArray,totalWeight):
    u = uniform(0,1)
    s=0
    i=0
    while(s<=totalWeight*u):
        s+=weightArray[i]
        i+=1
    return i-1

def norm(x):
    return (1/const)*exp(-math.pow(x,2)/2)

def importance(x,a):
    return math.exp(-(x-a))

def cauchy(x,a):
    return (1/pi)*(1/(math.pow(x-a,2)+1))

n = int(argv[1])
a = int(argv[2])
b = int(argv[3])
integ = []
impor = []
Mn = 0
counter = 0
k = 0
w=[]
sample = [a + ((b-a)*i/1000) for i in range(1001)]
#sample = [((b)*i/1000) for i in range(1001)]
squareArea = (b-a)*(norm(a))

#for i in sample:
#    k+=
#print(k)

print(len(sample))
for i in sample:
    w.append(math.exp(-(i-a)))
    #w.append(cauchy(i))
print(w)
W = math.fsum(w)
print(W)

for i in range(1,n+1):
    x_i = uniform(a,b)
    y_i = uniform(0,norm(a))
    if y_i <= norm(x_i): counter+=1
    integ.append(counter*squareArea/i)

    w_i = w[genSample(w,W)]
    Mn += (1/const)*math.exp(w_i-(math.pow(w_i,2)/2) -5)#norm(w_i)/importance(w_i,a) 
    impor.append(Mn/i)


print(1-(counter*squareArea/n))
print(1-impor[n-1])
plt.loglog(impor,color='blue', label='importance sampling')
plt.loglog(integ,color='red', label='integration method')
#plt.ylim(0,1)
plt.legend()
plt.show()
