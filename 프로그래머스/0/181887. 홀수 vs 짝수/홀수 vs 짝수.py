def solution(num_list):
    odd_res = 0
    even_res = 0
    for i in range(0,len(num_list),2):
        odd_res += num_list[i]
    for i in range(1,len(num_list),2):
        even_res += num_list[i]
    
    if odd_res > even_res:
        return odd_res
    else:
        return even_res