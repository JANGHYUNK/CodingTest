def solution(absolutes, signs):
    result = 0
    signs_num = 0

    for i in absolutes:
        if signs[signs_num] == True:
            result += i
        else:
            result -= i
    
        signs_num = signs_num + 1
    
    return result