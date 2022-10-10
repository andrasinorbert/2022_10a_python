"""
1. Az osztály tanulóinak magagassága névsor szerint:
170, 193, 186, 167, 175, 194, 164
Adjuk meg, névsor szerint hanyadik diák a 
    legalacsonyabb, és hanyadik a legmagasabb!
"""
# Max-kiválasztás
diakokMagassaga=[170, 193, 186, 167, 175, 194, 164]
MaxErt=diakokMagassaga[0]
MaxIndex=0
MinErt=diakokMagassaga[0]
MinIndex=0
for i in range(1,len(diakokMagassaga)):
    if(diakokMagassaga[i]>MaxErt):
        MaxErt=diakokMagassaga[i]
        MaxIndex=i
    if(diakokMagassaga[i]<MinErt):
        MinErt=diakokMagassaga[i]
        MinIndex=i
print("A legalacsonyabb diák a ", MinIndex+1, ".")
print("A legmagasabb diák a ", MaxIndex+1, ".")

"""
2. Az 1. feladatban található magasságok közül,
    hány diák magassága páros szám?
"""
#Megszámlálás
parosMagassagokSzama=0
for i in range(0,len(diakokMagassaga)):
    if(diakokMagassaga[i] % 2 == 0):
        parosMagassagokSzama=parosMagassagokSzama+1
print("A diákok közül",parosMagassagokSzama,"páros magasságú diák van")

"""
3. Adjuk meg, hogy mennyi az osztály átlagmagassága! (1.feladat)
"""
# Összegzés
magassagokOsszege=0
for i in range(0,len(diakokMagassaga)):
    magassagokOsszege+=diakokMagassaga[i]
atlagMagassag=magassagokOsszege/len(diakokMagassaga)
kerekitettatlag=round(atlagMagassag,1)
print("Az osztály átlagmagassága:",kerekitettatlag)

"""
4. Adjuk meg, hogy a névsor hanyadik diákja 167 cm magas!
"""
# Keresés
keresettMagassag=167
i=0
while i<len(diakokMagassaga) and not(diakokMagassaga[i]==keresettMagassag):
    i+=1
talaltE=i<len(diakokMagassaga)
if(talaltE):
    print("Találtunk",keresettMagassag,"cm magasságú diákot! A",i+1,". diák az!")
else:
    print("Nem volt",keresettMagassag,"cm magas diák az osztályban!")

"""
5. Van-e az osztályban 200cm-es diák?
"""
#Eldöntés
keresettMagassag=200
i=0
while i<len(diakokMagassaga) and not(diakokMagassaga[i]==keresettMagassag):
    i+=1
talaltE=i<len(diakokMagassaga)
#print("Van" if talaltE else "Nincs", "ilyen diák az osztályban")
if(talaltE):
    print("Van ilyen diák az osztályban")
else:
    print("Nincs ilyen diák az osztályban")

"""
6. Adjuk meg, hogy mennyi a magassága az első, páratlan
magasságértékű diáknak!
"""
# Kiválasztás
i=0
while not(diakokMagassaga[i]%2==1):
    i+=1
print("Az első páratlan értékű diák névsor szerint a", i+1,
      "., és magassága:", diakokMagassaga[i],"cm")