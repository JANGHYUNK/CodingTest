def solution(n, k):
    res =0
    res += n*12000
    service = n//10
    k -= service
    res += k*2000
    return res