def solution(num):
    result = 0

    if num == 1:
        return 0
    
    while result<500:
    
        result += 1
        if num % 2 == 0:
            num = int(num / 2)
        else:
            num = int(num * 3 + 1)

        if num == 1:
            return result
        if result == 500:
            return -1
    
        