a=12
b=18
def gcd(x,y):
    while y:
        x,y=y,x%y
    return x
lcm=(a*b)// gcd(a,b)
print("lcm of num is",lcm)

c=int(input("enter a 1st number:"))
d=int(input("enter a 2nd number:"))
def gcd(c,d):
    while(d):
        c,d=d,c%d
    return c
lcm=(c*d)//gcd(c,d)
print("lcm is",lcm)