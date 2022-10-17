# 1. feladat:
# Nyilvántartjuk a Savaria expresszre kiadott helyjegyeket.
# Van-e még szabad hely az expresszen
# Helyjegyek száma: 25
helyjegyek_eladva=[True, True, True, False, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True]
helyjegyek_eladva=[True, True, True, True]
helyjegyek_eladva=[False,False]

i=0
while i<len(helyjegyek_eladva)-1 and not(helyjegyek_eladva[i]==False):
    i=i+1
van_meg_hely=i<len(helyjegyek_eladva)-1
if van_meg_hely:
    print("Van még szabad hely")
else:
    print("Nincs már szabad hely")   


# 2. feladat:
# Határozzuk meg az N (>1) természetes számhoz legközelebbi négyzetszámot!
N= 101
i=N
import math
while not(math.sqrt(i)%1==0):
    i+=1
print(i)
