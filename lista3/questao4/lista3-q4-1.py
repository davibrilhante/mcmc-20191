from math import exp, pi, sqrt
from matplotlib import pyplot as plt
expo = []
norm = []
const = 1/(sqrt(2*pi))
samples = [-20+40*(i/1000) for i in range(1000)] 
print(const)
for i in samples:
    if i>=0:
        expo.append(exp(-i))
    else:
        expo.append(exp(i))
    norm.append(const*exp(-1*pow(i,2)/2))

plt.plot(expo, label='exponential')
plt.plot(norm, label='normal')
plt.legend()
plt.show()
