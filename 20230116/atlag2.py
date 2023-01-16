import fajlkezeles as f

filenev="20230116/input2.txt"
adatok=f.readfile_str_array(filenev)

str=adatok[0].split(' ')
sz=[]
for i in range(len(str)):
    sz.append(int(str[i]))
    
def atlag(sz_l):
    s=0
    for i in range(len(sz_l)):
        s+=sz_l[i]
    return s/len(sz_l)

print(atlag(sz))
