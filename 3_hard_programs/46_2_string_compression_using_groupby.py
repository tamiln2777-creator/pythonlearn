from itertools import groupby
s=input("enter a string:")
for k,g in groupby(s):   #k stores the string's character and g stores the group of characters list [2,2,2]
                         #groupby() groups consecutive identical elements together
    print((k,len(list(g))),end=" ")   #returns (character,number of times it occurs),(),()...