a=int(input("enter a number:"))
b=str(a)
b= b[::-1]
print(b)

c=234
r=0
while (c>0):
    r=r*10+c%10
    c=c//10
print(r)