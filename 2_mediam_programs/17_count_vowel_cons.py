a=input("enter a string:")
a=a.lower()
v,c=0,0
for ch in a:
    if ch.isalpha():
        if ch in "aeiou":
            v+=1
        else:
            c+=1
print("no of vowel is",v)
print("no of constant is",c)
