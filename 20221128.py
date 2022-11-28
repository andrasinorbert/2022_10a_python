def Sorozatszamitas(X, func, s=0):
    for i in range(len(X)):
        s=func(s, X[i])
    return s

def szorzas(a,b):
    return a*b
X=[1,2,3,4,5]

print(Sorozatszamitas(X, szorzas, 1))

def osszead(a,b):
    return a+b

print(Sorozatszamitas(X, osszead))

def Megszamlalas(X, func):
    c=0
    for i in range(len(X)):
        if(func(X[i])):
            c+=1
    return c

def paros_e(a):
    return a%2==0

print(Megszamlalas(X, paros_e))

def ptlan_e(a):
    return a%2==1

print(Megszamlalas(X, ptlan_e))

def maxkivalasztas(X):
    maxIndex=0
    maxErtek=X[0]
    for i in range(1, len(X)):
        if (X[i]>maxErtek):
            maxErtek=X[i]
            maxIndex=i
    return (maxIndex,maxErtek)

print(maxkivalasztas([4,3,5,2,6,1]))

def SzelsoertekKivalasztas(X, func):
    Index=0
    Ertek=X[0]
    for i in range(1, len(X)):
        if (func(X[i], Ertek)):
            Ertek=X[i]
            Index=i
    return (Index,Ertek)

def maximum(a,b):
    return a>b
def minimum(a,b):
    return a<b

print(SzelsoertekKivalasztas([4,3,5,2,6,1], minimum))
print(SzelsoertekKivalasztas([4,3,5,2,6,1], maximum))