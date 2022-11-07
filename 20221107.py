# Adott egy számokat tartalmazó A lista és egy B szám.
# Adjunk meg két olyan elemet az A-ból, amelyek szorzata éppen a B!

A=[2,3,4,5,6,7]
B=42

i=0 # A[i] =2
while True: # ebben a ciklusban változik i értéke
    j=i+1
    print(f"Külső: {i} {j}")
    while j<len(A) and A[i]*A[j]!=B:
        print(f"Belső: {i} {j}")
        j+=1
    if(j<len(A)):
        break;
    i+=1

print(f"A B({B}) szám az alábbi számok szorzata: {A[i]}, {A[j]}")