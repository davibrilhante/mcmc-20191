import math
from math import log
import random

pi = math.pi
quarterPi = pi/4
halfPi = pi/2
threeHalfPi =3*pi/2
twicePi = 2*pi 
class Antenna:
    def __init__(self,Type='FLAT_TOP', beams=8):
        self.type = Type
        self.gain = 0
        self.efficiency = 1
        self.beams = beams
        self.beamwidth = 2*pi/self.beams
        self.resolution = 1
        if Type=='FLAT_TOP':
            self.setFlatTop()
        elif Type=='CONE_PLUS_CIRCLE':
            self.setConePlusCircle()

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

def getReflectionPoints(transmitter, room, angle, beam, order):
    #RETURNS A TUPLE WITH THE LENGTH OF REFLECTED PATH, THE POINT OF REFLECTION
    #AND THE EDGE WHICH REFLECTED. THE POSITION IN THE ARRAY IS ALSO THE ORDER
    #OF REFLECTION
    refOrd = order+1
    rayCenter = beam2angle(transmitter,beam)
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
        point = [room.lenght, transmitter.y - (room.length - transmitter.x)*math.tan(twicePi-angle)]
        distance = (room.length - transmitter.x)/math.cos(twicePi - angle)
        print("7")
    elif angle >= 0 and angle < corners[2]:
        point = [room.length, transmitter.y + (room.width - transmitter.x)*math.tan(angle)]
        distance = (room.length - transmitter.x)/math.cos(angle)
        print("8")

    return [point, distance, refOrd]
