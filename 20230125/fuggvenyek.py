
def osszead(a,b):
    c=a+b
    print(c)
    
    
def kivon(a,b):
    c=a-b
    print(c)
    
def osszead_nemkiir(a,b):
    return a+b


def harmonikus_kozep(lista):
    _sum=0
    for i in lista:
        _sum= 1/i
    return len(lista)/_sum

def mertani_kozep(lista):
    _szorzat=1
    for i in lista:
        _szorzat*=i
    return _szorzat**(1/len(lista))

def szamtani_kozep(lista):
    _sum=0
    for i in lista:
        _sum+=i
    return _sum/len(lista)

def negyzetes_kozep(lista):
    _sum=0
    for i in lista:
        _sum+= i**2
    _sum=_sum/len(lista)
    return i**(1/2)

