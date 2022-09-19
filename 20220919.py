"""
class sajatOsztaly:
    def __new__(self, nev, kor):
        self.nev=nev
        self.kor=kor


nev = input("Add meg a neved: ")
kor = int(input("Add meg a korod(számmal): "))

en=sajatOsztaly(nev, kor)

print(sajatOsztaly.nev)
print(sajatOsztaly.kor)

print(type(en))
"""

list=[3,4,5,6,7,4,2, 7, 3]

print(list)
print(type(list))

print("összeg: "+str(sum(list)))

# Megszámlálás tétele nagyjából
counter=0
for i in list:
    counter+=1

print("átlag: ",sum(list)//counter)

nagyszam=1000

for i in list:
    print(nagyszam,"-",i,"=",nagyszam-i)
    nagyszam-=i

print(nagyszam)

# Összegzés tétele
sum=0
for i in list:
    sum+=i
print("lista elemek összege:", sum)

# Maximum keresés
lista=[-1000,-600, -200,-500]
max, index= -10000, 0
for i in lista:
    print("max:", max, "i:", i, "index:", index)
    if(max<i):
        max=i
    else:
        index+=1
print("Lista legnagyobb eleme:", max )
print("Legnagyobb elem indexe:", index)
# házi: megírni úgy hogy működjön