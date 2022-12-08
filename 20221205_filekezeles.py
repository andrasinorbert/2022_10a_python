f=open("input.txt", "rt")
print(f.read())
sorok=f.readlines()
f.close()
"""
f=open("input.txt", "a")
f.write("Sanyi")
f.close()

f=open("input.txt", "a")
f.write("\nSanyi")
f.close()

f=open("input.txt", "w")
f.write("Sanyi")
f.close()
"""
f=open("input.txt", "r")
sorok=f.readlines()
f.close()
vanebennerepjel=sorok[len(sorok)-1].find("\n")
newline='\n'
print(len(sorok)-1)
if not vanebennerepjel:
    sorok[len(sorok)-1]+=f"{newline}"
sorok.append("Adat500")
print(sorok)
f=open("input.txt", "w")
f.writelines(sorok)
f.close()


