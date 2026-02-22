import random
num=random.randint(1,10)
guss=int(input("enter a number between 1 to 10:"))
if guss==num:
    print("your guss is correct")
else:
    print("your guss is wrong the correct number is",num)