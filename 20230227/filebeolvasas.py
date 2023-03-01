f=open("20230227/input.txt", "r", encoding="utf-8")
sorok=f.readlines()
f.close()

nevek=[]
magassagok=[]

for sor in sorok:
    sor_1 = sor.strip()
    sor_2= sor_1.split(" ")
    nevek.append(sor_2[0])
    magassagok.append(int(sor_2[1]))
print(nevek)
print(magassagok)
