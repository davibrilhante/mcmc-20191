import classes
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import LogNorm
import math
import time
import interference

freq = 60e9
print("===============================================\n................Creating Antenna...............")
start_time = time.time()
antenna = classes.Antenna('UNIFORM_CIRCULAR_ARRAY', 8, freq)
#antenna.plotAntennaPattern()
print(time.time() - start_time)

print("===============================================\n.................Creating Nodes................")
#create tx
tx = classes.Node(75.0,75.0)
tx.antenna = antenna
tx.antenna.gain = tx.antenna.gain[180:] + tx.antenna.gain[:180]
#create rx
rx = classes.Node(75.0,135.0)
rx.antenna = antenna
rx.antenna.gain = rx.antenna.gain[270:] + rx.antenna.gain[:270]


print("===============================================\n.................Creating Room.................")
#create Room
room = classes.Room(150.0, 150.0)
#interferers = interference.createInterferer(room,10)
#status = interference.hardcoreModel(interferers, 100)

print("===============================================\n................Creating Channel...............")
#create channel
los = True
channel = classes.Channel(los)

print("===============================================\n.............Starting Simulation...............")
samples = 10000
#nInterfer = 5
leng = 100
result = [[0 for j in range(leng)] for i in range(leng)]

start_time = time.time()
for i in range(100):
    for j in range(100):
        if j == 50 and i == 50:
            continue
        x = 1.5*i#np.random.rand()*room.length
        y = 1.5*j#np.random.rand()*room.width

        angleTx = classes.angleToPoint(tx,x,y) 
        angleRx = classes.angleToPoint(rx,x,y)
        if round(angleTx,1) == round(2*math.pi,1): angleTx = 0
        if round(angleRx,1) == round(2*math.pi,1): angleRx = 0
        print(angleTx, angleRx)
        gainTx = tx.antenna.gain[180+int(math.degrees(angleTx))]
        gainRx = rx.antenna.gain[180+int(math.degrees(angleRx))]
        loss = channel.linkBudgetPoint(tx,x,y,freq)
        linkBudget = tx.txPower + gainTx + gainRx - loss
        pInterfer = 0
    #    for j in range(nInterfer):
    #        intNode = classes.Node(np.random.rand()*room.length, np.random.rand()*room.width)
    #        angleInt = classes.angleToPoint(intNode,x,y)
    #        intNode.antenna = antenna
    #        randomAngle = np.random.rand()*360
    #        intNode.antenna.gain = intNode.antenna.gain[randomAngle:] + intNode.antenna.gain[:randomAngle]
    #        gainNode = intNode.antenna.gain[180+int(math.degrees(angleInt))]
    #        lossInt = channel.linkBudgetPoint(intNode,x,y,freq)
    #        pInterfer += intNode.txPower + gainNode + gainRx - lossInt
    #    for m in range(len(status)):
    #        for n in range(len(status[m])):
    #            if status[m][n] == 1:
    #                
        result[int(x*leng/(room.length))][int(y*leng/room.width)] = linkBudget

print(time.time() - start_time)

maxs = [max(i) for i in result]
mins = [min(i) for i in result]


minmin = min(mins)
maxmax = max(maxs)
#print(minmin,maxmax)
for i in range(leng):
    for j in range(leng):
        result[i][j] = (result[i][j] - minmin)/(maxmax - minmin)

c = plt.pcolor(result, cmap='jet')
cb = plt.colorbar(c)#, ticks=[minmin + i*((maxmax - minmin)/5) for i in range(5)]) 
cb.set_ticks([0 + i*0.2 for i in range(6)], update_ticks=True)
cb.set_ticklabels([round(minmin + i*((maxmax - minmin)/5),2) for i in range(6)], update_ticks=True)
plt.show()
#print(result)
