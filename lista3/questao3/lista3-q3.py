from urllib import request
from http import client
from random import choice
from string import ascii_lowercase as alphabet
from sys import argv

def generateString(length):
    letters = alphabet
    return ''.join(choice(letters) for i in range(length))

n = int(argv[1])
counter = 0
domain = "www.xyzw.ufrj.br"
req = client.HTTPConnection(domain)
req.request("HEAD",'')
print(req.getresponse().status)
print(req)
for i in range(n):
    domain = 'www.'+generateString(4)+'.ufrj.br'
    print(domain)
    req = client.HTTPConnection(domain).request("HEAD", '')
    print(req)
    if (request.urlopen(domain).getcode())==200:
        counter+=1
print(counter/n)
