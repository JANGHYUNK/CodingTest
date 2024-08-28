def solution(a, b, n):
    answer = 0
    remain_bottle = 0
    while n>=a:
        if n % a == 0:    
            n = (n // a) * b       
            answer += n   
        
        else:
            remain_bottle = n % a   
            n = (n // a) * b  
            answer += n   
            n += remain_bottle 
            
    return answer


