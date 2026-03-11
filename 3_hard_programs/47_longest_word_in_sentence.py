s=input("enter the sentence:").split()
lon=""
for i in s:
    if len(i)>len(lon):
        lon=i
print("longest word in the sentence is :",lon)