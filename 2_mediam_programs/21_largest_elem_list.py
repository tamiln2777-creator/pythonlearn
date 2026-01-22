lst=input("enter a number:").split()
a=lst[0]
for i in lst:
    if i>a:
        a=i
print("largest num is ",a)
