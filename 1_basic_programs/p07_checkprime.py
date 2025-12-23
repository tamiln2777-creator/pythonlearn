a=7
if(a>1):
    for i in range(2,a):
        if a%i==0:
            print("not a prime number")
            break
    else:
        print("prime number")
else:
    print("negative num")


b=int(input("enter a number:"))
if(b>1):
    for i in range(2,b):
        if b%i==0:
            print("Not a prime number")
            break
    else:
        print("prime number")
else:
    print("negative number not allowed")