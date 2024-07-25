def solution(n):
    a = int(n ** 0.5) 
    if n == (a**2):
        return ((a+1)**2)
    else:
        return (-1)