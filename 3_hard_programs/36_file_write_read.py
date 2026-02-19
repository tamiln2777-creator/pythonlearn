f=open("sample.text","w")
f.write("hello world")
f.close()


r=open("sample.text","r")
print(r.read())
f.close()