import classes
import math

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
for a in angles:
    print(classes.getReflectionPoints(n1,r1,a,0,0))
