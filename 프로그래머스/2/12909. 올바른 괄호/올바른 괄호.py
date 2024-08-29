def solution(s):
    stack = []


    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if stack:
                stack.pop()
            else:
                return False
                break
    else:
        if not stack:
            return True
        else:
            return False