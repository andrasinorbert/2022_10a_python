f=open("20230306/input.txt", "r", encoding="utf-8")
sorok=f.readlines()
f.close()

nevek=[]
magassagok=[]

for i in range(len(sorok)):
    sor=sorok[i]
    sor_2=sor.strip()
    sor_3=sor_2.split(" ")
    nev=sor_3[0]
    magassag=int(sor_3[1])
    nevek.append(nev)
    magassagok.append(magassag)
print(nevek)
print(magassagok)
    