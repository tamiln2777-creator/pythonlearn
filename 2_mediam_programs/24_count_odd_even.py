lst=[1,2,3,9,8,7]
even,odd=0,0
for i in lst:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("even:",even)
print("odd:",odd)
