def solution(left, right):
    res = 0

    for i in range(left,right+1):
        answer = 0
        for j in range(1,i+1):
            if i % j == 0:
                answer += 1
        if answer % 2 == 0:
            res += i
        else:
            res -= i
    return res
           
