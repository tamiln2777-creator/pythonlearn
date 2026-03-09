lst=list(map(int,input("enter the list of numbers: ").split()))
tar=int(input("enter the target number: "))
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]+lst[j]==tar:
            print("the indices of the two numbers are: ",i,j)