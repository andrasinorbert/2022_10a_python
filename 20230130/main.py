def readfile_int_array(filenev):
    f=open(filenev, "r")
    sorok=f.readlines()
    f.close()
    ret=[]
    for i in sorok:
        sor=i.split(" ")
        for j in sor:
            ret.append(int(j.strip()))
    return ret

def negyzetesKozep(lista):
    """Egy szám listának a négyzetes közepét adja vissza

    Args:
        lista ( list ): számlista

    Returns:
        int: Négyzetes közép
    """
    
    osszeg=0
    for i in lista:
        osszeg+= pow(i,2) # i**2
    osszeg= 1/len(lista)
    return osszeg**(1/2) #sqrt(osszeg)

mappa="20230130/"
filename=mappa+"input.txt"
lista=readfile_int_array(filename)
osszeg=sum(lista)
print(osszeg)
print(negyzetesKozep(lista))

filename=mappa+"input2.txt"
f=open(filename, "r",encoding="utf-8")
sorok=f.readlines()
f.close()
print(sorok)

nev_lista=[]
magassag_lista=[]
for i in sorok:
    sor=i.split()
    nev_lista.append(sor[0])
    magassag_lista.append(int(sor[1]))

for i in range(len(nev_lista)):
    print("név: "+nev_lista[i] + "; magasság: "+ str(magassag_lista[i]))

max_index=0
max_ertek=magassag_lista[0]
for i in range(len(magassag_lista)):
    if(max_ertek<magassag_lista[i]):
        max_ertek=magassag_lista[i]
        max_index=i
        
print(str(max_ertek)+" "+str(max_index) +" "+nev_lista[max_index])

filename=mappa+"output.txt"
f=open(filename,'w')
f.write(nev_lista[max_index]+"; "+str(max_ertek))
f.close()

f=open(filename,'a')
f.write("valami")
f.close()

min_index=0
min_ertek=magassag_lista[0]
for i in range(len(magassag_lista)):
    if(min_ertek>magassag_lista[i]):
        min_ertek=magassag_lista[i]
        min_index=i
print(str(min_index)+" "+str(min_ertek))

filename=mappa+"output.csv"
f=open(filename,'w', encoding="utf-8")
f.write(nev_lista[min_index]+"; "+str(min_ertek))
f.close()

filename=mappa+"output.csv"
f=open(filename,'r', encoding="utf-8")
sorok=f.readlines()
f.close()

nev_lista=[]
magassag_lista=[]
for i in sorok:
    sor=i.split(";")
    nev=sor[0]
    szam=sor[1].strip()
    nev_lista.append(nev)
    magassag_lista.append(szam)
print(nev_lista)
print(magassag_lista)
