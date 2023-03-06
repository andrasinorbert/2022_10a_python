f=open("20230306/input3.txt", "r", encoding="utf-8")
sorok=f.readlines()
f.close()

nevek=[]
magassagok=[]
korok=[]

for i in range(1,len(sorok)):
    sor=sorok[i]
    sor_2=sor.strip()
    sor_3=sor_2.split(" ")
    nev=sor_3[0]
    magassag=int(sor_3[1])
    kor=int(sor_3[2])
    nevek.append(nev)
    magassagok.append(magassag)
    korok.append(kor)

print(nevek)
print(magassagok)
print(korok)

def atlagSzamitas(lista):
    s=0
    for i in range(len(lista)):
        if lista[i]%2==0:
            s+=lista[i]
    atlag=s / len(lista)
    return atlag
    """
    return sum(lista)/len(lista)
    """

print(atlagSzamitas(magassagok))
print(atlagSzamitas(korok))

