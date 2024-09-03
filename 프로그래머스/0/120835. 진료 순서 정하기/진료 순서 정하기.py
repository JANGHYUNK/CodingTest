def solution(emergency):    
    res = []
    B = sorted(emergency,reverse=True)
    for i in range(len(B)):
        res.append(B.index(emergency[i])+1)

    print(res)
    return res