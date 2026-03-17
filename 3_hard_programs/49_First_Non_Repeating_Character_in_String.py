s=input("enter the string:")
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in d:
    if d[i]==1:
        print("the non-repeating character is:",i)
        break
else:
    print("there is no non-repeating character in the string")