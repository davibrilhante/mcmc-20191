#!/usr/bin/env python3

import math
from numpy import dot as mult
from numpy import array as array
from matplotlib import pyplot as plt

def totalVarDist(alpha,beta):
    res=0
    if len(alpha)==len(beta):
        for i,j in zip(alpha, beta):
            res += abs(i-j)
        return res/2
    else:
        print("Arrays length does not match!")

n = 1024
sqr = int(math.sqrt(n))
mixtureTime = 10000
pi0 = array([1] + [0 for i in range(n-1)])

################## ANEL ###########################
piAnel = array([1/n for i in range(n)])
pAnel = [[0 for j in range(n)] for i in range(n)]

################# ARVORE ##########################
den1 = 2*(n-1)
piArv = [2/den1]+[0 for i in range(n-1)]
pArv = [[0 for j in range(n)] for i in range(n)]
pArv[0] = [0.5, 0.25, 0.25]+[0 for i in range(n-3)]
piArv[0] = 1/(n-1)

############### RETICULADO ########################
piRet = [0 for i in range(n)]
pRet = [[0 for j in range(n)] for i in range(n)]
quinas = [0,sqr,n-sqr,n-1]
den2 = 2*(2*n - 2*sqr)

for i in range(n):
        pAnel[i][i] = 0.5

        if i==n-1:
            pAnel[i][0] = 0.25
        else:
            pAnel[i][i+1] = 0.25
        pAnel[i][i-1] = 0.25

for i in range(n):
        pRet[i][i] = 0.5
        ########### RETICULADO ##########
        #   > Quina
        if quinas.count(i)!=0:
            piRet[i] = 2/den2
            if i==0 or i==sqr-1:
                pRet[i][i+sqr] = 0.25
            if i==0 or i==n-sqr:
                pRet[i][i+1] = 0.25
            if i==n-sqr or i==n-1:
                pRet[i][i-sqr] = 0.25
            if i==sqr-1 or i==n-1:
                pRet[i][i-1] = 0.25
        #   > Bordas
        elif (i>0 and i<sqr-1): 
            piRet[i]=3/den2
            pRet[i][i-1] = 1/6
            pRet[i][i+1] = 1/6
            pRet[i][i+sqr] = 1/6
        elif (i>n-sqr and i<n-1):
            piRet[i]=3/den2
            pRet[i][i-1] = 1/6
            pRet[i][i+1] = 1/6
            pRet[i][i-sqr] = 1/6
        elif (i%sqr == sqr-1):
            piRet[i]=3/den2
            pRet[i][i-1]=1/6
            pRet[i][i+sqr] = 1/6
            pRet[i][i-sqr] = 1/6
        elif (i%sqr == 0):
            piRet[i]=3/den2
            pRet[i][i+1]=1/6
            pRet[i][i+sqr] = 1/6
            pRet[i][i-sqr] = 1/6
        #   > Meio
        else:
            piRet[i] = 4/den2
            pRet[i][i+1]=1/8
            pRet[i][i-1]=1/8
            pRet[i][i+sqr] = 1/8
            pRet[i][i-sqr] = 1/8
            
#        if i>=n/2:
#           1 
base = math.log(n,2)
for i in range(n):
    pArv[i][i]=1/2
    if i == 0:
        pArv[i][i+1]=1/4
        pArv[i][i+2]=1/4
    elif i>=(math.pow(2,base-1)-1):
        piArv[i]=1/den1
        if i%2 == 0:
            pArv[i][int(i/2)-1]=1/2
        else:
            pArv[i][int(i/2)]=1/2
    else:
        piArv[i]=3/den1
        if i%2 == 0:
            pArv[i][int(i/2)-1]=1/6
        else:
            pArv[i][int(i/2)]=1/6
        pArv[i][(2*i)+1]=1/6
        pArv[i][(2*i)+2]=1/6


piAnel = array(piAnel)
piArv = array(piArv)
piRet = array(piRet)

piTAnel = pi0.dot(pAnel)
resAnel = [totalVarDist(piTAnel,piAnel)]

piTRet = pi0.dot(pRet)
resRet = [totalVarDist(piTRet,piRet)]

piTArv = pi0.dot(pArv)
resArv = [totalVarDist(piTArv,piArv)]

for t in range(mixtureTime-1):
    piTAnel = piTAnel.dot(pAnel)
    resAnel.append(totalVarDist(piTAnel,piAnel))

    piTRet = piTRet.dot(pRet)
    resRet.append(totalVarDist(piTRet,piRet))

    piTArv = piTArv.dot(pArv)
    resArv.append(totalVarDist(piTArv,piArv))

plt.grid(True,which="both",ls="-")
plt.loglog(range(mixtureTime), resAnel,label='Anel')
plt.loglog(range(mixtureTime), resRet,label='Reticulado')
plt.loglog(range(mixtureTime), resArv,label='Arvore')
plt.legend()
plt.savefig('lista4-q3-1.png')
plt.show()
