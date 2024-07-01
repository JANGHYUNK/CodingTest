def solution(num_list, n):
    result = []
   
    b = len(num_list)
    for i in range(0,b,n):
        result.append(num_list[i:i+n]) 
    return result