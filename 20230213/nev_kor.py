f=open("20230213\\nev_kor.txt", "r", encoding="utf-8")
adat=f.readlines()
f.close()
print(adat)

nevek=[]
korok=[]
for i in adat:
    l=i.split(";")
    nevek.append(l[0])
    kor=int(l[1].strip())
    korok.append(kor)
print(nevek)
print(korok)

maxertek=korok[0]
maxindex=0
for i in range(len(korok)):
    if maxertek<korok[i]:
        maxertek=korok[i]
        maxindex=i
print(nevek[maxindex])