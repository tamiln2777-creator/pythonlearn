a=12
b=26
while(b):
    a,b=b,a%b
print("gcd is",a)

c=int(input("enter a number:"))
d=int(input("enter a number:"))
while(d):
    c,d=d,c%d
print("gcd is",c)