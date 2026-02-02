lst=[10,20,9,20,10,55]
rev=[]
for i in lst:
    if i not in rev:
        rev.append(i)
print(rev)

lst1=input().split()
lst1=list(map(int,lst1))
r=[]
for i in lst1:
    if i not in r:
        r.append(i)
print(r)