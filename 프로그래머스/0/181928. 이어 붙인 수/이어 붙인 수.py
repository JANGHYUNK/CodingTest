def solution(num_list):
    
    result_even = ""
    result_odd = ""
    for i in num_list:
        if i % 2 == 1:
            result_odd += str(i)
        else:
            result_even += str(i)
    result = int(result_odd) + int(result_even)
    print(result)
    return result