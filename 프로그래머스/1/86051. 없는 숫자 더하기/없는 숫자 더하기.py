def solution(numbers):
    res = 0

    for i in range(0,10):
        if (i in numbers) == False:
            res += i
    return res