def solution(money):

    result1 = 0
    reuslt2 = 0
    result = []
    result1 = int(( money / 5500 ))
    result.append(result1)
    result2 = int(( money % 5500 ))
    result.append(result2)
    
    return result