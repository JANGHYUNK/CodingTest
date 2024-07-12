def solution(n):
   
    n =list(map(int,str(n)))
    n.sort(reverse = True)
    res = ""
    for i in n:
        res += str(i)
    return int(res)