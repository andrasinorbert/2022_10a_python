# 1.nap: 1 Ft
# 2.nap: 2 Ft
# 3.nap: 4 Ft
# 4.nap: 8 Ft
#.....
# 30.nap: 2^29 Ft

import math


napiutalasokLista=list()

napiutalasokLista.append(1)
napiutalasokLista.append(2)

# print(napiutalasokLista)
index=2
while index<30:
    napiutalasokLista.append(math.pow(2,index))
    # print(index+1,napiutalasokLista[index])
    index+=1

s=0
for i in range(len(napiutalasokLista)):
    s+=napiutalasokLista[i]

print("Hó végére összesen", s,"Ft pénz lesz a számlámon")

# Az előző egyszerűbben
s=0
for i in range(30):
    s+=math.pow(2,i)
    print(i,s)
print("Hó végére összesen", s,"Ft pénz lesz a számlámon")

import random

lista=list()

for i in range(10000):
    list.append(random.randint(100,1000))

# 10000 random egész szám közül, melyikből van a legtöbb?
szamok=dict()

for i in lista:
    

