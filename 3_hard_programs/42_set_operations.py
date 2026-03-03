a={1,2,3,4,5}
b={4,5,6,7,8}
print("Union of sets a and b:",a.union(b))      #print(a|b) also gives the same result
print("Intersection of sets a and b:",a.intersection(b)) #a&b
print("Difference of sets a and b:",a.difference(b))     #a-b
print("Symmetric difference of sets a and b:",a.symmetric_difference(b))  #a^b
print("Is a subset of b?",a.issubset(b))       #Checks if all elements of a are inside b
print("Is a superset of b?",a.issuperset(b))   #Checks if a contains all elements of b.
print("Is a disjoint with b?",a.isdisjoint(b))   #Checks if a and b have no common elements.