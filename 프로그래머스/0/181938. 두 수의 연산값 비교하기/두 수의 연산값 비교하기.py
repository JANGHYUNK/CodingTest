def solution(a, b):
    str1 = str(a) + str(b)
    str2 = 2 * a * b
    if int(str1) > str2:
        return int(str1)
    elif int(str1) < str2:
        return str2
    else:
        return int(str1)    