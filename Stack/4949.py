while True:
    case_string = input()
    stack = []

    if case_string == ".":
        break

    for char in case_string:
        if char == "(" or char == "[":
            stack.append(char)
        elif char == ")":
            if  stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(char)
                break
        elif char == "]":
            if   stack and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(char)
                break

    if not stack:
        print("yes")
    else:
        print("no")

