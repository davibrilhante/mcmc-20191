from random import uniform
from sys import argv
from math import cos, pi, sqrt
from matplotlib import pyplot as plt
counter = 0
error=[]
sqrt2 = sqrt(2)
n=int(argv[1])
for i in range(1,n+1):
    x_i = uniform(0,pi/4)
    y_i = uniform(0,4/pi)
    if y_i <= cos(x_i): counter+=1
    e_n = 2*counter/i
    error.append(abs(e_n - sqrt2)/sqrt2)

plt.loglog(error)
plt.grid(True,which="both",ls="-")
print(counter)
plt.show()
