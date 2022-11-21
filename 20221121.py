def FV_1(X,B):
    for i in range(len(X)):
        X[i]=X[i]+B
    return X

print(FV_1([1,2,3,4], 5))

def FV_3(X):
    for i in range(1,len(X)):
        X[i-1]=X[i]
    X[len(X)-1]=0
    return X

print(FV_3([2,3,4]))

def FV_3_v2(X):
    for i in range(len(X)):
        X[i]=X[i+1]
    X[len(X)-1]=0
    return X
#print(FV_3_v2([2,3,4,5]))

def FV_4(X):
    tmp=X[0]
    for i in range(1,len(X)):
        X[i-1]=X[i]
    X[len(X)-1]=tmp
    return X
print(FV_4([2,3,4,5]))