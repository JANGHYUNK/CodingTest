def solution(n):
    str1 = "수박"
    
    if n % 2 == 0:
        num = n/2
        return (str1*int(num))
    else:
        num = n/2
        return (str1 * int(num) + "수")