from matplotlib import pyplot as plt
from scipy import special as sp
import math

pi = math.pi

Lambda = 3/600
theta0 = pi/2
phi0 = 0
space = Lambda/2
radius = Lambda/2
nElements = 6


plt.plot([-180+i for i in range(360)],gain)
plt.show()

