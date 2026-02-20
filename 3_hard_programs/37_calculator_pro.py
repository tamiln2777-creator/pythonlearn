a=int(input("Enter a number: "))
b=int(input("enter another number:"))
op=input("enter an operator from +,-,*,/: ")

match op:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "/":
        if b==0:
            print("division by error")
        else:
            print(a/b)
    case "_":
        print("Invalid operator")
        