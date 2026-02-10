a=int(input("enter a num:"))
temp=a
sum=0
l=len(str(a))
while temp>0:
    sum+=pow((temp%10),l)
    temp//=10
if a==sum:
    print("armstrong num")
else:
    print("not a armstrong num")
