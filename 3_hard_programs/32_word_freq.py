a=input("enter a string:")
a=a.split()
dic={}
for i in a:
    if i not in dic:
        count=a.count(i)
        dic[i]=count
print(dic)