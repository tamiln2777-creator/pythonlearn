a=12345
sum=0
while (a>0):
    sum+=a%10
    a//=10
print("the sum is",sum)

b=int(input("enter a number:"))
s=0
while(b>0):
    s+=b%10
    b=b//10
print("the sum of digits is",s)
