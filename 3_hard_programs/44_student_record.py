stu={}
n=int(input("enter the number of students:"))
for i in range(n):
    name=input("enter the name of student:")
    marks=(input("enter the marks of student:"))
    stu[name]=marks
for i in stu:
    print(i,stu[i])