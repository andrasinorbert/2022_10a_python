f=open("20230227/input2.txt", "r", encoding="utf-8")
sorok=f.readlines()
f.close()

input=dict({
    "rendszámok": [],
    "távolság": []
})


input["rendszámok"].append("abc-123")



rendszamok=[]
tavolsag=[]

for sor in sorok:
    sor_1 = sor.strip()
    sor_2= sor_1.split(" ")
    rendszamok.append(sor_2[0])
    tmp=[]
    for i in range(1,len(sor_2)):
        tmp.append(int(sor_2[i]))
    tavolsag.append(tmp)
    
print(rendszamok)
print(tavolsag)

def osszestavolsag(lista):
    s=0
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            s+=lista[i][j]
    return s

def nullakszama(lista):
    c=0
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if(lista[i][j]==0):
                c+=1
    return c

print(osszestavolsag(tavolsag))
print(nullakszama(tavolsag))
