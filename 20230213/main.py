f=open("20230213\input.txt", "r", encoding="utf-8")
adat=f.readlines()
f.close()
print(adat)

f=open("20230213\input.txt", "a", encoding="utf-8")
f.write("\nvalami2")
f.close()


f=open("20230213\input2.txt", "w", encoding="utf-8")
f.write("Gizi;165")
f.close()

lista=["első sor\n", "második sor\n", "harmadik sor"]
f=open("20230213\output.txt", "w", encoding="utf-8")
f.writelines(lista)
f.close()



f=open("20230213\output.txt", "r", encoding="utf-8")
sorok=f.readlines()
f.close()
print(sorok)

f=open("20230213\output.txt", "w", encoding="utf-8")
f.writelines(sorok[:-1])
f.close()