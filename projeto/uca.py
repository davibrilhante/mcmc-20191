from matplotlib import pyplot as plt
from scipy import special as sp
from numpy import random
import math
import threading
from sys import argv
pi = math.pi

def ucaArrayFactor(nElements, freq, theta0, phi0, radius, theta, phi):
    Lambda = 3e8/freq
    space = Lambda/2
    k = 2*pi/Lambda

    parcel1 = math.sin(theta)*math.sin(phi) - math.sin(theta0)*math.sin(phi0)
    parcel2 = math.sin(theta)*math.cos(phi) - math.sin(theta0)*math.cos(phi0)

    csi = math.atan2(parcel1,parcel2)
    ro = radius*math.sqrt(math.pow(parcel2,2)+math.pow(parcel1,2))
    arg = k*ro
    summ = 0
    for m in range(1,20):
        summ+=(1j**(m*nElements))*sp.jv(m*nElements, arg)*math.cos(m*nElements*csi)

    af = abs(sp.jv(0,arg) - 2*summ)

    return af 

def mcIntegration(result,index, n, nElements, freq, theta0, phi0, radius):
    Mn = 0
    for i in range(n):
        u = random.rand()
        p = random.rand()*pi
        t = random.rand()*2*pi
        
        z = ucaArrayFactor(nElements, freq, theta0, phi0, radius, t, p)
        z = math.pow(z,2)*math.sin(t)
        if u <= z:
            Mn += 1
    result[index]=Mn
    return 0
    
def ucaAntennaGain(nElements, freq, theta0, phi0, radius, theta, phi):
    Lambda = 3e8/freq
    space = Lambda/2
    k = 2*pi/Lambda

    af = ucaArrayFactor(nElements, freq, theta0, phi0, radius, theta, phi)

    n = 1000
#    Mn = 0
#    for i in range(n):
#        u = random.rand()
#        p = random.rand()*pi
#        t = random.rand()*2*pi
#        
#        z = ucaArrayFactor(nElements, freq, theta0, phi0, radius, t, p)
#        z = math.pow(z,2)*math.sin(t)
#        if u <= z:
#            Mn += 1
    nThreads = 100
    runs = int(n/nThreads)
    t = [0 for i in range(nThreads)]
    T = []
    for i in range(nThreads):
        T.append(threading.Thread(target=mcIntegration, args=(t,i,runs,nElements, freq, theta0, phi0, radius)))
        T[i].daemon = True
        T[i].start()
        T[i].join()
    Mn = sum(t)
    integral = 2*math.pow(pi,2)*(Mn/n)
    gain = 4*pi*math.pow(af,2)/integral
    return 10*math.log10(gain)

def ucaPlotGain(nElements,freq):
    gain = []
    theta0 = pi/2
    phi0 = 0
    radius = (nElements*(3e8/freq))/(4*pi)#float(argv[3])*(3e8/freq)
    theta = pi/2
    for i in range(-180,180):
        phi = math.radians(i)
        gain.append(ucaAntennaGain(nElements, freq, theta0, phi0, radius, theta, phi))
    plt.plot([-180+i for i in range(360)],gain)
    plt.ylim(-5,15)
    plt.show()

def ucaPlotAf(nElements,freq):
    AF = []
    theta0 = pi/2
    phi0 = 0
    radius = (nElements*(3e8/freq))/(4*pi)#float(argv[3])*(3e8/freq)
    theta = pi/2
    for i in range(-180,180):
        phi = math.radians(i)
        AF.append(ucaArrayFactor(nElements, freq, theta0, phi0, radius, theta, phi))
    plt.plot([-180+i for i in range(360)],AF)
    plt.show()

#if __name__=="__main__":
#    ucaPlotAf(8,60e9)
#    ucaPlotGain(8,60e9)
