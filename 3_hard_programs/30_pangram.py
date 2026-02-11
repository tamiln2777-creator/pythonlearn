a=input("enter a string:").lower()
count=0
for i in "abcdefghijklmnopqrstuvwxyz":
    if i in a:
        count+=1
print("pangram:",count)
