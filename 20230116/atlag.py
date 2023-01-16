f=open("20230116/input.txt", "r")
#print(f.read())
sorok=f.readlines()
f.close()

def sorvegjel_torlese(s):
    if(s[-1]=='\n'):
        return s[:-1]
    else:
        return s

for i in range(len(sorok)):
    sorok[i]=sorvegjel_torlese(sorok[i])

#for i in sorok:
    #print(i + " tipus: "+ str(type(i)))
    #for c in i:
    #    print(int(c))
szamlista=[]
for i in range(len(sorok)):
    szamlista.append(int(sorok[i]))

print(szamlista)

def atlag(sz_l):
    s=0
    for i in range(len(sz_l)):
        s+=sz_l[i]
    return s/len(sz_l)

print("A fájlban található számok átlaga: "
      +str(atlag(szamlista)))