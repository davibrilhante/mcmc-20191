import math
from matplotlib import pyplot as plt
import numpy as np
import classes

def createInterferer(room, space):
    interferers = []
    for i in range(int(room.length/space)):
        interferers.append([])
        for j in range(int(room.width/space)):
            interferers[i].append(classes.Node((i*space)+space,(j*space)+space))
    return interferers

def hardcoreModel(interferers, mixture):
    nNodes = len(interferers)*len(interferers[0])
    counter = mixture
    status = [[0 for j in interferers[0]] for i in interferers]
    while counter != 0:
        counter -= 1
        node = np.random.rand()*nNodes
        i = int(node/len(interferers[0]))
        j = int(node%len(interferers[0]))
        if status[i][j]==0:
            if np.random.rand() > 0.5:
                if i==0:
                    if j==0:
                        if status[i][j+1]==0 and status[i+1][j]==0:
                            status[i][j]=1
                    elif j==len(interferers[i])-1:
                        if status[i][j-1]==0 and status[i+1][j]==0:
                            status[i][j]=1
                    else:
                        if status[i][j-1]==0 and status[i][j+1]==0 and status[i+1][j]==0:
                            status[i][j]=1
                elif i==len(interferers)-1:
                    if j==0:
                        if status[i][j+1]==0 and status[i-1][j]==0:
                            status[i][j]=1
                    elif j==len(interferers[i])-1:
                        if status[i][j-1]==0 and status[i-1][j]==0:
                            status[i][j]=1
                    else:
                        if status[i][j-1]==0 and status[i][j+1]==0 and status[i-1][j]==0:
                            status[i][j]=1
                else:
                    if j == 0:
                        if status[i][j+1]==0 and status[i+1][j]==0 and status[i-1][j]==0:
                            status[i][j] = 1
                    if j == len(interferers[i])-1:
                        if status[i][j-1]==0 and status[i+1][j]==0 and status[i-1][j]==0:
                            status[i][j] = 1
                    else:
                        if status[i][j-1]==0 and status[i][j+1]==0 and status[i+1][j]==0 and status[i-1][j]==0:
                            status[i][j]=1
                
        elif status[i][j]==1:
            if np.random.rand()>0.5:
                status[i][j] = 0
    return status
