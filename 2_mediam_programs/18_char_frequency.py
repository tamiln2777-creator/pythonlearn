a=input("enter a string:")
f={}
for i in a:
    if i in f:
        f[i]+=1
    else:
        f[i]=1
print(f)