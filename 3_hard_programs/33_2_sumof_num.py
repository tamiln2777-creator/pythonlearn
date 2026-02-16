#for two numbers....
a=input("enter a string:")
tot=0
num=""
for i in a:
    if i.isdigit():
        num+=i
    else:
        if num!="":
            tot+=int(num)
            num=""
if num!="":
    tot+=int(num)
print("total is",tot)