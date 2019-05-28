#!/usr/bin/env python3

import math
from sys import argv
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
<<<<<<< HEAD
#[[226, 3634,58158], [77, 383,1694,7117], [31, 76,125,172]]
N = [int(argv[1])]#[256,1024]#[10,50,100]#,300,700,1000,3000,5000,10000]
=======
#[[226, 3634,58158], [77, 383,1694i,7117], [31, 76,125,172]]
N = [256,1024]#[10,50,100]#,300,700,1000,3000,5000,10000]
>>>>>>> refs/remotes/origin/master
T = [[],[],[]]
epsilon=0.0001

for n in N:
    sqr = int(math.sqrt(n))
    pi0 = [1] + [0 for i in range(n-1)]
    pi0 = array(pi0)
    t = [1,1,1]
    condition=[False,False,False]

    ################## ANEL ###########################
    piAnel = array([1/n for i in range(n)])
    pAnel = [[0 for j in range(n)] for i in range(n)]

    ################# ARVORE ##########################
    den1 = 2*(n-2)
    piArv = [2/den1]+[0 for i in range(n-2)]
    pArv = [[0 for j in range(n-1)] for i in range(n-1)]
    pArv[0] = [0.5, 0.25, 0.25]+[0 for i in range(n-4)]
    piArv[0] = 1/(n-2)

    ############### RETICULADO ########################
    piRet = [0 for i in range(n)]
    pRet = [[0 for j in range(n)] for i in range(n)]
    quinas = [0,sqr-1,n-sqr,n-1]
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

    base = math.log(n,2)
    for i in range(n-1):
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



    piArv = array(piArv)

    piRet = array(piRet)

    piTAnel = pi0.dot(pAnel)
    resAnel = totalVarDist(piTAnel,piAnel)

    piTRet = pi0.dot(pRet)
    resRet = totalVarDist(piTRet,piRet)
    
    pi0 = array([1] + [0 for i in range(n-2)])
    piTArv = pi0.dot(pArv)
    resArv = totalVarDist(piTArv,piArv)

    while (condition[0]!=True) or (condition[1]!=True) or (condition[2]!=True):
        if resAnel >= epsilon:
            piTAnel = piTAnel.dot(pAnel)
            resAnel = totalVarDist(piTAnel,piAnel)
            condition[0]=False
            t[0]+=1
            if t[0]%100==0:
                print(t[0],resAnel)
        else: 
            print("Anel",t[0],resAnel)
            condition[0]=True

        if resRet >= epsilon:
            piTRet = piTRet.dot(pRet)
            resRet = totalVarDist(piTRet,piRet)
            condition[1]=False
            t[1] += 1
        else:
            print("Ret",t[1],resRet)
            condition[1]=True

        if resArv >= epsilon: 
            piTArv = mult(piTArv, pArv)
            resArv = totalVarDist(piTArv,piArv)
            condition[2]=False
            t[2]+=1
            if t[2]%100==0:
                print(t[2],resArv)
        else: 
            print("Arv",t[2],resArv)
            condition[2]=True

    T[0].append(t[0])
    T[1].append(t[1])
    T[2].append(t[2])
    
    print(n," Ok!")

print(T)
plt.grid(True,which="both",ls="-")
#plt.plot(range(len(T[0])),T[0],label='Anel')
#plt.plot(range(len(T[1])),T[1],label='Reticulado')
#plt.plot(range(len(T[2])),T[2],label='Arvore')
plt.semilogy(range(len(T[0])),T[0],label='Anel')
plt.semilogy(range(len(T[1])),T[1],label='Reticulado')
plt.semilogy(range(len(T[2])),T[2],label='Arvore')
plt.legend()
plt.savefig('lista4-q3.png')
plt.show()
