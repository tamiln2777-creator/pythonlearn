a=input("enter a string:")
res=""
for i in a:
    if i not in res:
        res+=i
print(res)