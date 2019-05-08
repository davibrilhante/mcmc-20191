#!/usr/bin/env python3

from urllib import request
from random import choice, uniform, seed
from string import ascii_lowercase as alphabet
from sys import argv

def generateString(length):
    letters = alphabet
    return ''.join(choice(letters) for i in range(length))

n = int(argv[1])
#s = int(argv[2])
#seed(s)
found = []
counter1 = 0
counter2 = 0
for i in range(n):
    counter1+=1
    k = int(uniform(2,5))
    domain = "http://www."+generateString(k)+".ufrj.br"
    #if i == 1: domain = "http://www.land.ufrj.br"
    if found.count(domain) == 0:
        try:
            request.urlopen(domain).getcode()
            print(domain,k,i)#(s*n)+i)
            counter2+=1
            found.append(domain)
        except:
            pass
print(counter2/n)
