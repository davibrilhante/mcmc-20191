import math
from numpy import dot as mult
from numpy import array as array
from matplotlib import pyplot as plt

n = 1024
sqr = int(math.sqrt(n))
mixtureTime = 500
pi0 = [1] + [0 for i in range(n-1)]

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
den2 = 4*n*(n-1)

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
            if i==sqr-n or i==n-1:
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
    elif i> math.pow(2,base-2):
        piArv[i]=1/den1
        pArv[i][int(i/2)]=1/2
    else:
        piArv[i]=3/den1
        pArv[i][int(i/2)]=1/6
        pArv[i][(2*i)+1]=1/6
        pArv[i][(2*i)+2]=1/6


piArv = array(piArv)

piRet = array(piRet)

pi1 = mult(pi0,pAnel)
piTAnel = pi1
resAnel = [sum(abs(piTAnel - piAnel))]

pi1 = mult(pi0,pRet)
piTRet = pi1
resRet = [sum(abs(piTRet - piRet))]

pi1 = mult(pi0,pArv)
piTArv = pi1
resArv = [sum(abs(piTArv - piArv))]

for t in range(mixtureTime-1):
    piTAnel = mult(piTAnel, pAnel)
    resAnel.append(sum(abs(piTAnel-piAnel)))

    piTRet = mult(piTRet, pRet)
    resRet.append(sum(abs(piTRet-piRet)))

    piTArv = mult(piTArv, pArv)
    resArv.append(sum(abs(piTArv-piArv)))

print(piTAnel)
print(resAnel)

plt.grid(True,which="both",ls="-")
plt.loglog(range(mixtureTime), resAnel,label='Anel')
plt.loglog(range(mixtureTime), resRet,label='Reticulado')
plt.loglog(range(mixtureTime), resArv,label='Arvore')
plt.legend()
plt.savefig('lista4-q3.png')
plt.show()
