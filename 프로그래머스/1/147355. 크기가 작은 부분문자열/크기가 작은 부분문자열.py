def solution(t, p):
    result = 0
    ans = []
    M_len = len(t)-len(p)

    for i in range(M_len+1): 
        ans.append(t[0+i:len(p)+i])
    
    for i in range(len(ans)):
        if int(ans[i]) <= int(p):
            result += 1
        
    return result