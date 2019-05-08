import math
from math import log
import random

pi = math.pi
class Antenna:
    def __init__(self,Type='dir', gain=10, beams=8):
        self.type = Type
        self.gain = gain
        self.beams = beams
        self.beamwidth = 2*pi/self.beams
    def setFlatTop():
        self.gain = 10*log(self.beams)
    #def setUCA():
    #transformar o ganho em um vetor com 360 elementos, um para cada grau ao 
    #redor do no
        
class Node:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Room:
    def __init__(self,width,height):
        self.width = width
        self.height = heigth
        self.nObjects = 0
        self.objects = []

class Object:
    def __init__(self,material='body',n):
        self.material = material
        self.nCorners = n
        self.corner = []
        self.loss = 42

    def setCorners(self,cornerArray):
        if len(cornerArray)==self.nCorners:
            self.corner = cornerArray
        else:
            return "Corner Array dimension and number of desirable coners must match"

    def setRandomCorners(self,n):
        
class Channel:
    def __init__(self):
        self.model = 'LOG_NORMAL_NO_SHADOW'
    def setType(self,channelType):
        self.model = channelType
    def linkBudget(tx,rx,los):
        if self.model == 'LOG_NORMAL_NO_SHADOW':
            if los==True:
                1
            else:
                1
        elif self.model == 'LOG_NORMAL':
            if los==True:
                1
            else:
                1
        elif self.model == 'TWO_RAY_RICE':
            1
        elif self.model == 'ONE_RAY_RICE':
            1

def findAnchor(transmitter, receiver, room):
    1
