def solution(s):
    s_len = len(s)

    if s_len % 2 == 0:
        return s[int(s_len/2)-1:int(s_len/2)+1]
    else:
        return s[int(s_len/2)]
    
    