s = input("enter the parentheses: ")

stack = []

pairs = {
    ")": "(",
    "}": "{",
    "]": "["
}

for ch in s:

    if ch in "({[":
        stack.append(ch)

    else:
        if not stack or stack[-1] != pairs[ch]:
            print("invalid")
            break

        stack.pop()

else:
    if not stack:
        print("valid")
    else:
        print("invalid")