class Person:
    def __init__(self, _nev, _magassag, _kor):
        self.nev=_nev
        self.kor=_kor
        self.magassag=_magassag
        
    def __str__(self) -> str:
        return f"név:{self.nev}; magasság:{self.magassag}; kor:{self.kor}"
        
    def kiir(self):
        print(self.nev, self.magassag, self.kor)

def magassagatlag(list):
    s=0
    for i in list:
        s+=i.magassag
    return s/len(list)


f=open("20230320/input1.txt", encoding="utf-8")
sorok=f.readlines()
f.close()

szemelyek=[]

for i in range(1,len(sorok)):
    sor_1=sorok[i].strip()
    sor_2=sor_1.split(";")
    obj=Person(sor_2[0], int(sor_2[1]), int(sor_2[2]))
    szemelyek.append(obj)

for i in szemelyek:
    i.kiir()

for i in szemelyek:
    print(i)

print(magassagatlag(szemelyek))