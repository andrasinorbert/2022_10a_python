"""
A napokat a 00 választja el egymástól
Az adatok, hogy az adott távolságot hány perc alatt
    futotta le az illető
Feladat: A napi átlag kiszámítása
"""

f=open("20230306/input5.txt", "r", encoding="utf-8")
sorok=f.readlines()
f.close()

futasok=[]
napieredmeny=[]

for i in range(len(sorok)):
    sor=sorok[i]
    sor_2=sor.strip()
    adat=int(sor_2)
    if adat==0:
        futasok.append(napieredmeny)
        napieredmeny=[]
    else:
        napieredmeny.append(adat)
print(futasok)

def atlag(lista):
    return sum(lista)/len(lista)

for i in range(len(futasok)):
    print(f"A(z) {i}. napon az átlag: {round(atlag(futasok[i]),1)}")
