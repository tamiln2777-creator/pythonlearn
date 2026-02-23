lst=list(map(int,input("enter a list of numbers:").split()))
lst1=[]
for i in lst:
    if i in lst1:
        continue
    else:
        lst1.append(i)
        if lst.count(i)>1:
            print(i,end=" ")