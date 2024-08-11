def solution(a, b):
    res = []
    for i,j in zip(a,b):
        p = i*j
        res.append(p)
    return sum(res)