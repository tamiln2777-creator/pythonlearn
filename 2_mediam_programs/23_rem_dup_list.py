lst=[10,20,9,20,10,55]
rev=[]
for i in lst:
    if i not in rev:
        rev.append(i)
print(rev)
