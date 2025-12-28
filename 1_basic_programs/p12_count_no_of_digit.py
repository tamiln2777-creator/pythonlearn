a=12345
count=0
while(a>0):
    a//=10
    count+=1
print("no of digits is",count)

b=int(input("enter a number:"))
b=str(b)
print("the number of digits is",len(b))