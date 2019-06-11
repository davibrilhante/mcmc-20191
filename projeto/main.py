import classes
import numpy as np
from matplotlib import pyplot as plt
import math

freq = 60e9
print("====================================\n.................Creating Nodes................")
#create tx
tx = classes.Node(1.0,5.0)
tx.antenna.setUCA(freq)

#create rx
rx = classes.Node(9.0,5.0)
rx.antenna.setUCA(freq)

print("====================================\n.................Creating Room.................")
#create Room
room = classes.Room(10.0, 10.0)

print("====================================\n................Creating Channel...............")
#create channel
los = True
channel = classes.Channel(los)

print("====================================\n.............Starting Simulation...............")
samples = 10000
result = [[0 for j in range(samples)] for i in range(samples)]
for i in range(samples):
    x = np.random.rand()*room.length
    y = np.random.rand()*room.width

    angleTx = classes.angleToPoint(tx,x,y) 
    angleRx = classes.angleToPoint(rx,x,y)
    gainTx = tx.antenna.gain[int(math.degrees(angleTx))]
    loss = channel.linkBudgetPoint(tx,x,y,freq)
    linkBudget = tx.txPower + gainTx - loss
    result[x][y] = linkBudget

#plt.pcolor(result, cmap=plt.cm.Reds)
#plt.show()
