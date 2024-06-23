def solution(n_str):
    a = list(n_str)
    while a[0] == '0':  
        del a[0]  
    return ''.join(a) if a else '0'