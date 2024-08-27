def solution(numbers, direction):
    if direction == "right":
        R = numbers.pop()
        numbers.insert(0,R)
    else:
        L = numbers[0]
        del numbers[0]
        numbers.append(L)
    
    return numbers