def solution(x, n):
    answer = []
    for i in range(1,n+1):
        xi = x*i
        answer.append(xi)
    return answer