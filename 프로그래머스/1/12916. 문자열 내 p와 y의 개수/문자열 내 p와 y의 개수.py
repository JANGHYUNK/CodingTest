def solution(s):
    pNum = 0
    yNum = 0
    for i in s:
        if "p" == i:
            pNum += 1
        elif "P" ==i:
            pNum += 1    
        elif "y" == i:
            yNum += 1
        elif "Y" == i:
            yNum += 1
    print(pNum)
    print(yNum)
    if pNum == 0 and yNum == 0:
        return True
    elif pNum == yNum:
        return True
    elif pNum != yNum:
        return False
    