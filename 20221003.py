#lista
lista=[ 1,2,3,4]
lista2=lista

print(lista)
print(lista2)

lista2[2]=7
print("lista2[2]=7 módosítás után: ",lista)
print("lista2[2]=7 módosítás után: ",lista2)

lista3=lista[:]
lista3[3]=8
print("lista3[3]=8 módosítás után: ",lista)
print("lista3[3]=8 módosítás után: ",lista3)