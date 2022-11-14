# Ismerjük a versenyzől indulási és érkezési idejét
# Ki a győztes?

versenyzok= [
    # indulási idő, érkezési idő
    ("10:00", "10:50"),
    ("10:10", "10:55"),
    ("10:20", "11:00"),
    ("10:30", "11:10"),
    ("10:40", "11:40"),
    ("10:50", "11:29")
]

# szét kell bontani a stringet órára percre
# return tuple-> (óra, perc)
def idoSzetbontas(ido):
    ido_lista=ido.split(':')
    return (int(ido_lista[0]), int(ido_lista[1]))

# éjféltől eltelt percek számítása
# paraméter: (óra, perc)
# paraméterben tuple
def elteltPercSzamito(ido):
    ora=ido[0]
    perc=ido[1]
    return ora*60+perc

# mennyi a különbség érkezés, indulás közt
# return érkezésiIdo-indulásiIdo
def versenyIdoSzamitas(indulasIdo, erkezesiIdo):
    return erkezesiIdo-indulasIdo

# eredeti listából -> csak eltelt perceket tartalmazó listát ad eredményül
def mindenkiVersenyidejenekSzamiasa(lista):
    """
    lista= [
        ("10:00", "10:50"),
        ("10:10", "10:55")
    ]
    """
    eredmenyek=[]
    for i in range(len(lista)):
        # lista[i]= ("10:00", "10:50")
        indulas=idoSzetbontas(lista[i][0]) # (10,0)
        erkezes=idoSzetbontas(lista[i][1]) # (10,50)
        indulas_perc=elteltPercSzamito(indulas)
        erkezes_perc=elteltPercSzamito(erkezes)
        ido=versenyIdoSzamitas(indulas_perc,erkezes_perc)
        eredmenyek.append(ido)
    return eredmenyek

X=mindenkiVersenyidejenekSzamiasa(versenyzok)
print(X)
    
# paraméter lista, ami tuple-öket tartalmaz
# minimum kiv tétel
def elsoHelyezett( lista):
    minErt=X[0]
    minIndex=0
    for i in range(len(X)):
        if( X[i] < minErt):
            minErt=X[i]
            minIndex=i
    return (minIndex, minErt)

eredmeny=elsoHelyezett(X)
print(eredmeny)


