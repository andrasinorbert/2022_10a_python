def sortores_torlese(s):
    if(s[-1]=='\n'):
        return s[:-1]
    else:
        return s

def readfile_str_array(filenev):
    f=open(filenev, "r")
    sorok=f.readlines()
    f.close()
    
    clean_sorok=[]
    for i in range(len(sorok)):
        clean_sorok.append(sortores_torlese(sorok[i]))
    return clean_sorok