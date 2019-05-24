import math
from numpy import dot as mult
from numpy import array as array
from matplotlib import pyplot as plt

n = 1000
sqr = math.sqrt(n)
mixtureTime = 500
pi0 = [1] + [0 for i in range(n-1)]

################## ANEL ###########################
piAnel = array([1/n for i in range(n)])
pAnel = [[0 for j in range(n)] for i in range(n)]

################# ARVORE ##########################
piArv = array([0 for i in range(n)])
pArv = [[0 for j in range(n)] for i in range(n)]
pArv[0] = [0.5, 0.25, 0.25]+[0 for i in range(n-3)]
piArv[0] = 1/(n-1)
den1 = 2(n-1)

############### RETICULADO ########################
piRet = array([0 for i in range(n)])
pRet = [[0 for j in range(n)] for i in range(n)]
quinas = [0,99,990,999] 
den2 = 4*n*(n-1)

for i in range(n):
        pAnel[i][i] = 0.5
        pArv[i][i] = 0.5
        pRet[i][i] = 0.5

        if i==n-1:
            pAnel[i][0] = 0.25
        else:
            pAnel[i][i+1] = 0.25
        pAnel[i][i-1] = 0.25

        if quinas.count(i)<>0:
            piRet[i] = 2/den2
            if i==0 or i==99:
                pRet[i][i+sqr] = 0.25
            if i==0 or i==990:
                pRet[i][i+1] = 0.25
            if i==990 or i==999:
                pRet[i][i-sqr] = 0.25
            if i==99 or i==999:
                pRet[i][i-1] = 0.25
        if (i>0 and i<99): 
            piRet[i]=3/den2
            pRet[i][i-1] = 1/6
            pRet[i][i+1] = 1/6
            pRet[i][i+sqr] = 1/6
        if (i>990 and i<999):
            piRet[i]=3/den2
            pRet[i][i-1] = 1/6
            pRet[i][i+1] = 1/6
            pRet[i][i-sqr] = 1/6
            

        if i>=n/2:
            

pi1 = mult(pi0,pAnel)
piT = pi1
resAnel = [sum(abs(piT - piAnel))]
print(resAnel)

for t in range(mixtureTime-1):
    piT = mult(piT, pAnel)
    resAnel.append(sum(abs(piT-piAnel)))

print(piT)
print(resAnel)

plt.loglog(range(mixtureTime), resAnel)
plt.show()
