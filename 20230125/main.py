import fuggvenyek

fuggvenyek.osszead(4,5)
fuggvenyek.osszead(5,6)
fuggvenyek.osszead(6,7)

x=[]
x[0]=fuggvenyek.osszead_nemkiir(4,5)
x[1]=fuggvenyek.osszead_nemkiir(5,6)

_sum=0
for i in x:
    _sum+=i
_atlag=_sum/len(x)


z=[2,4,6,8,5,3,2]
har_kozep=fuggvenyek.harmonikus_kozep(z)


