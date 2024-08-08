def solution(arr, divisor):

    arr_plus = list()
    if divisor == 1:
        arr_new = sorted(arr)       
        return arr_new
    
    for i in arr:
        if (i % divisor) == 0:
            arr_plus.append(i)
            arr_plus.sort()
    
    if arr_plus == [] :
        arr_plus = [-1]
        return arr_plus
    return arr_plus