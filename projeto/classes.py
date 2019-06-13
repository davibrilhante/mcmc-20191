import math
from math import log
import random
from matplotlib import pyplot as plt
from scipy import special as sp
import numpy as np
import uca

pi = math.pi
quarterPi = pi/4
halfPi = pi/2
threeHalfPi =3*pi/2
twicePi = 2*pi 
class Antenna:
    def __init__(self,Type='FLAT_TOP', beams=8,freq=60e9):
        self.type = Type
        self.gain = 0
        self.efficiency = 1
        self.beams = beams
        self.beamwidth = 2*pi/self.beams
        self.resolution = 1
        self.arrayFactor = []
        self.nElements = 8
        if Type=='FLAT_TOP':
            self.setFlatTop()
        elif Type=='CONE_PLUS_CIRCLE':
            self.setConePlusCircle()
        elif Type=='UNIFORM_CIRCULAR_ARRAY':
            self.setUCA(freq)

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

    def setUCA(self,freq):
        radius = (self.nElements*(3e8/freq))/(4*pi)
        theta0 = halfPi
        phi0 = 0
        theta = halfPi
        #self.arrayFactor = [uca.ucaArrayFactor(self.nElements, freq, radius, theta0, phi0, theta, math.radians(i)) for i in range(-180,180)]
        self.gain = []
        for i in range(-180,180):
            phi = math.radians(i)
            self.gain.append(uca.ucaAntennaGain(self.nElements, freq, theta0, phi0, radius, theta, phi))
    
    def plotAntennaPattern(self):
        plt.plot([-180+i for i in range(360)],self.gain)
        plt.show()
        
class Node:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.txPower = 24 #transmission power in dBm
        self.sense = -90 #receiver sensitivity in dBm
        self.antenna = Antenna()

class Room:
    def __init__(self,width,length):
        self.width = width
        self.length = length
        self.height = 0
        self.nObjects = 0
        self.objects = []

class Object:
    def __init__(self, x, y, material, corners):
        self.material = material
        self.nCorners = corners
        self.corner = []
        if self.material == "plywood":
            self.loss = 59 #loss in db
        elif self.material == "aluminium":
            self.loss = 56 #loss in db
        elif self.material == "brickwall":
            self.loss = 59 #loss in db
        elif self.material == "body":
            self.loss = 42 #loss in db
        self.heigth = 0

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
    def __init__(self,los):
        #path loss model
        self.largeScale = 'LOG_NORMAL_NO_SHADOW'
        #fading model
        self.smallScale = ''
        if los == True:
            self.shadowDeviation = 4.9 #in dB
            self.plExponent = 2.1
        else:
            self.shadowDeviation = 7.6 #in dB
            self.plExponent = 3.3

    def setType(self,channelType):
        self.model = channelType
    #def pathLoss(self):
    def linkBudgetNode(self,tx,rx,freq):
        comp = 3e8/freq
        dist = math.hypot(tx.x-rx.x, tx.y-rx.y)
        plRef = 20*math.log10(4*pi/comp)+10*self.plExponent*math.log10(dist)+np.random.normal(0,self.shadowDeviation) #+sum of obstacle attenuations
        return plRef
    def linkBudgetPoint(self,tx,pointx,pointy,freq):
        comp = 3e8/freq
        dist = math.hypot(tx.x-pointx, tx.y-pointy)
        plRef = (20*math.log10(4*pi/comp))+(10*self.plExponent*math.log10(dist))+np.random.normal(0,self.shadowDeviation) #+sum of obstacle attenuations
        return plRef
        

#        largeScale = [np.random.randn() for i in range(7)]
#        delaySpread = 10**(0.3*largeScale[0]-6.8)
#        aodSpread = 10**(0.42*largeScale[1]+1.1)
#        aoaSpread = 10**(0.36*largeScale[2]+1.3)
#        zodSpread = 10**(0.32*largeScale[3]+max((-0.002*dist+1.05),0.4))
#        zoaSpread = 10**(0.26*largeScale[4]+max((-0.0025*dist+1.1),0.3))
#        zoaBias = 10**(0.3*largeScale[5]+max((-0.0022*dist+1.36),0.6))
#        zoaSpread = 10**(0.3*largeScale[6]+max((-0.0017*dist+1.09),0.4))
#        XPRS = 10**(np.random.normal(15,2)/10)
#        if self.model == 'LOG_NORMAL_NO_SHADOW':
#        elif self.model == 'LOG_NORMAL':
#        elif self.model == 'TWO_RAY_RICE':
#        elif self.model == 'ONE_RAY_RICE':

def getQuadrant(angle):
    if angle>=0 and angle<= quarterPi:
        return 1
    elif angle>quarterPi and angle<=halfPi:
        return 2
    elif angle>halfPi and angle<=threeHalfPi:
        return 3
    elif angle>threeHalfPi and angle<= twicePi:
        return 4

def beam2angle(node, beam):
    #RETURN THE CENTER OF THE BEAM IN THE COMMON ORIENTATION
    return (beam+0.5)*node.antenna.beamwidth

def getBestBeam():
    1
def getReflectionEdges(transmitter, room):
    #Edge1 = (0,0) - (0,l)
    edge1 = math.atan2(-transmitter.y,-transmitter.x)
    #Edge2 = (0,l) - (w,l)
    edge2 = math.atan2(-transmitter.y,(room.length - transmitter.x))
    #Edge3 = (w,l) - (w,0)
    edge3 = math.atan2((room.width - transmitter.y),(room.length - transmitter.x))
    #Edge4 = (0,w) - (0,0)
    edge4 = math.atan2((room.width - transmitter.y), -transmitter.x)
    return [edge1,edge2,edge3,edge4]

def getReflectionPoints(transmitter, room, angle,order):
    #RETURNS A TUPLE WITH THE LENGTH OF REFLECTED PATH, THE POINT OF REFLECTION
    #AND THE EDGE WHICH REFLECTED. THE POSITION IN THE ARRAY IS ALSO THE ORDER
    #OF REFLECTION
    refOrd = order+1
    corners = getReflectionEdges(transmitter, room)
#    print([math.degrees(i) for i in corners])

    if angle >= corners[2] and angle < halfPi:
        point = [transmitter.x + (room.width - transmitter.y)/math.tan(angle), room.width]
        distance = (room.width - transmitter.y)/math.sin(angle)
        print("1")
    elif angle >= halfPi and angle <corners[3]:
        point = [transmitter.x - (room.width - transmitter.y)*math.tan(angle-halfPi), room.width]
        distance = (room.width - transmitter.y)/math.sin(angle-halfPi)
        print("2")

    elif angle >= corners[3] and angle < pi:
        point = [0, transmitter.y + math.tan(pi - angle)*transmitter.x]
        distance = (transmitter.x)/math.cos(pi - angle)
        print("3")
    elif  angle > pi and (angle - twicePi) < corners[0]:
        point = [0, transmitter.y - math.tan(angle-pi)*transmitter.x]
        distance = (transmitter.x)/math.cos(angle-pi)
        print("4")

    elif (angle-twicePi) >= corners[0] and angle < threeHalfPi:
        point = [transmitter.x - transmitter.y/math.tan(angle - pi),0]
        distance = transmitter.y/math.sin(angle - pi)
        print("5")
    elif angle >= threeHalfPi and (angle - twicePi )< corners[1]:
        point = [transmitter.x + transmitter.y*math.tan(angle-threeHalfPi),0]
        distance = transmitter.y/math.cos(angle)
        print("6")

    elif (angle - twicePi) >= corners[1] and angle < twicePi:
        point = [room.length, transmitter.y - (room.length - transmitter.x)*math.tan(twicePi-angle)]
        distance = (room.length - transmitter.x)/math.cos(twicePi - angle)
        print("7")
    elif angle >= 0 and angle < corners[2]:
        point = [room.length, transmitter.y + (room.width - transmitter.x)*math.tan(angle)]
        distance = (room.length - transmitter.x)/math.cos(angle)
        print("8")
    else:
        print("Nada!")

    return [point, distance, refOrd]

def reflectionAngle(transmitter, room, point, angle):
    if transmitter.y > point[0][1] and point[0][0]==0:
        return twicePi - angle
    elif transmitter.y < point[0][1] and point[0][0]==0:
        return twicePi - (angle - pi)
    elif transmitter.y > point[0][1] and point[0][0] == room.length:
        return twicePi - (angle - pi)
    elif transmitter.y < point[0][1] and point[0][0] == room.length:
        return pi - angle
    else:
        return twicePi - angle


def buildReflections(transmitter, room, angle, nReflections):
    reflectedPath = []
    counter = 0
    newAngle = angle
    while counter<nReflections:
        if counter == 0:
            reflectedPath.append(getReflectionPoints(transmitter, room, angle,counter))
        else:
            fakeNode = Node(reflectedPath[counter-1][0][0],reflectedPath[counter-1][0][1])
            ### quem eh o new angle
            newAngle = reflectionAngle(transmitter, room, reflectedPath[counter-1], newAngle)
            reflectedPath.append(getReflectionPoints(fakeNode, room, newAngle, counter))
        counter += 1
    return reflectedPath


def angleToPoint(transmitter, pointx, pointy):
    angle = math.atan2(transmitter.y - pointy, transmitter.x - pointx)
#    if angle>= 0:
    return angle
#    else:
#        return twicePi + angle

def angleBetweenNodes(transmitter, receiver):
    return angleToPoint(transmitter, receiver.x, receiver.y)
            

#def getObjectOnThePath(transmitter,room, refPoint):
#    projections = []
#    for obj in room.objects:
#        maxX = 0
#        maxY = 0
#        minX = room.length
#        minY = room.width
#        for i in obj.corners:
#            if i[0] > maxX:
#                maxX = i[0]
#            if i[0] < minX:
#                minX = i[0]
#            if i[1] > maxY:
#                maxY = i[1]
#            if i[1] < minY:
#                minY = i[1]
#        projections.append([minX,maxX,minY,maxY])
#
#    for p in projections:
#        if refPoint[0][0] < transmitter.x:
#            if refPoint[0][1]<transmitter.y:
#            elif refPoint[0][1]>transmitter.y:
#
#        elif refPoint[0][0] > transmitter.x:
#            if refPoint[0][1]<transmitter.y:
#            elif refPoint[0][1]>transmitter.y:
