def solution(myString):
    
    result = ""
    for i in myString:
        if i == 'a':
            result += i.upper()
        elif i == 'A':
            result += i
        else:
            result += i.lower()
        
    print(result)
    return result