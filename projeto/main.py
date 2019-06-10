import classes
import math
from matplotlib import pyplot as plt

pi = math.pi

a1 = classes.Antenna()
a1.setFlatTop()
a2 = classes.Antenna()
a2.setConePlusCircle()

print(a1.gain)
print(a2.gain)


n1 = classes.Node(1,2)
r1 = classes.Room(3,5)
angles = [pi/4, 3*pi/4, 5*pi/4, 7*pi/4]
#for a in angles:
#    print(classes.getReflectionPoints(n1,r1,a,0))

reflections = classes.buildReflections(n1,r1,angles[3],3)
print(reflections)

x = [n1.x] + [i[0][0] for i in reflections]
y = [n1.y] + [i[0][1] for i in reflections]

print(x)
print(y)


plt.plot(x,y)
plt.ylim(0,r1.width)
plt.xlim(0, r1.length)
plt.show()
