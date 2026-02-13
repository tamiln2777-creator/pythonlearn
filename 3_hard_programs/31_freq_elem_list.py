lst=[1,2,3,3,4,1,3,5]
count=0
for i in lst:
    c=lst.count(i)
    if c>count:
        count=c
        element=i
print("most repeated element is",element,"in", count,"times")