lst=list(map(int,input("enter the list of numbers:").split()))
for i in range(1,lst[-1]+1):
    if i not in lst:
        print(i)