import classes
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import LogNorm
import math
import time

freq = 60e9
print("===============================================\n................Creating Antenna...............")
start_time = time.time()
antenna = classes.Antenna('UNIFORM_CIRCULAR_ARRAY', 8, freq)
#antenna.plotAntennaPattern()
print(time.time() - start_time)

print("===============================================\n.................Creating Nodes................")
#create tx
tx = classes.Node(1.0,5.0)
tx.antenna = antenna

#create rx
rx = classes.Node(9.0,5.0)
rx.antenna = antenna


print("===============================================\n.................Creating Room.................")
#create Room
room = classes.Room(10.0, 10.0)

print("===============================================\n................Creating Channel...............")
#create channel
los = True
channel = classes.Channel(los)

print("===============================================\n.............Starting Simulation...............")
samples = 10000
leng = 100
result = [[0 for j in range(leng)] for i in range(leng)]
for i in range(samples):
    x = np.random.rand()*room.length
    y = np.random.rand()*room.width

    angleTx = classes.angleToPoint(tx,x,y) 
    angleRx = classes.angleToPoint(rx,x,y)
    gainTx = tx.antenna.gain[int(math.degrees(angleTx))]
    loss = channel.linkBudgetPoint(tx,x,y,freq)
    linkBudget = tx.txPower + gainTx - loss
    result[int(x*leng/(room.length))][int(y*leng/room.width)] = linkBudget

maxs = [max(i) for i in result]
mins = [min(i) for i in result]


minmin = min(mins)
maxmax = max(maxs)
print(minmin,maxmax)
for i in range(leng):
    for j in range(leng):
        result[i][j] = (result[i][j] - minmin)/(maxmax - minmin)

c = plt.pcolor(result, cmap='jet')
plt.colorbar(c) 
plt.show()
print(result)
