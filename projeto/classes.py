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
    def setFlatTop(self):
        #Considering an antenna pattern with -180 to 180 
        self.gain = [0 for i in range(360)]
        for i in range(360):
            g1 = 10*log(self.beams)
            if i-180 >= -int(math.degrees(self.beamwidth/2)) and i-180 <= int(math.degrees(self.beamwidth/2)):
                self.gain[i] = g1
            else:
                self.gain[i] = 0
    def setConePlusCircle(self):
        self.gain = [0 for i in range(360)]
        for i in range(360):
            g1 = 10*log(self.beams)
            g2 = 10*log(2*pi/(2*pi - self.beamwidth))
            if i-180>= -int(math.degrees(self.beamwidth/2)) and i-180 <= int(math.degrees(self.beamwidth/2)):
                self.gain[i] = g1
            else:
                self.gain[i] = g2
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
    def __init__(self, material, corners):
        self.material = material
        self.nCorners = corners
        self.corner = []
        self.loss = 42

    def setCorners(self,cornerArray):
        if len(cornerArray)==self.nCorners:
            self.corner = cornerArray
        else:
            return "Corner Array dimension and number of desirable coners must match"

    def setRandomCorners(self,n):
        1
        
class Channel:
    '''
    Premisses:
    - There are K paths
    - Time invariant gain
    - Each scattered path (in a given angle theta) has an delay
    - Received power and antenna gain pattern are functions of angle theta
    '''
    def __init__(self):
        #path loss model
        self.largeScale = 'LOG_NORMAL_NO_SHADOW'
        #fading model
        self.smallScale = ''
    def setType(self,channelType):
        self.model = channelType
    #def pathLoss(self):
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
