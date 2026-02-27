d={"a":3,"b":2,"c":1}
for i in sorted(d,key=d.get):
    print(i,d[i])