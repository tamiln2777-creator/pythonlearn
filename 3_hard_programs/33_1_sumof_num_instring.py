# for single number
a=input("enter a string:")
sum=0
for i in a:
    if i.isdigit():
        sum+=int(i)
print("total is",sum)