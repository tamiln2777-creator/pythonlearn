a=50
b=69
c=4
if a>b and a>c:
    print(a,"is largest")
elif b>c and b>a:
    print(b,"is largest")
else:
    print(c,"is largest")

x=int(input("enter a number 1:"))
y=int(input("enter a number 2:"))
z=int(input("enter a number 3:"))

if x>y and x>z:
    print(x,"is largest")
elif y>z:
    print(y,"is largest")
else:
    print(z,"is largest")