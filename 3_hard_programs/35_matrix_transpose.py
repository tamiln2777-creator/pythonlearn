m=[[1,2],[3,4]]
t=[]
for i in range(len(m[0])):  #range contain 2 because the number of columns in the matrix is 2  , you going to use i for columns transition
    r=[]
    for j in range(len(m)):   # range contain 2 because the number of rows in the matrix is 2 , you going to use j for rows transition
        r.append(m[j][i])    #1st loop fetch 1 and 2nd 3 
    t.append(r)
print(t)


# getting input from user for matrix 
'''m = []

for i in range(2):  # 2 rows
    row = []
    for j in range(2):  # 2 columns
        value = int(input(f"Enter value for position ({i},{j}): "))
        row.append(value)
    m.append(row)

print("Matrix:")
for row in m:
    print(*row)'''
