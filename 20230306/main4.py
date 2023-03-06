f=open("20230306/input4.txt", "r", encoding="utf-8")
sorok=f.readlines()
f.close()

szamok=[]

for i in range(len(sorok)):
    sor=sorok[i]
    sor_2=sor.strip()
    sor_3=sor_2.split(" ")
    tmp=[]
    for j in range(len(sor_3)):
        adat=sor_3[j]
        adat_int=int(adat)
        tmp.append(adat_int)
    szamok.append(tmp)
    
print(szamok)

def atlag_soronkent(lista):
    return sum(lista)/len(lista)

for i in range(len(szamok)):
    print(f"Az {i+1}. sor átlaga: {atlag_soronkent(szamok[i])}")
    print("Az "+str(i+1)+". sor átlaga:", atlag_soronkent(szamok[i]))

def atlag_osszes():
    s=0
    c=0
    for i in range(len(szamok)):
        for j in range(len(szamok[i])):
            s+=szamok[i][j]
            c+=1
    return s/c

print(atlag_osszes())