def solution(a, b, c):
    if a != b and a != c and b != c:
        return (a+b+c)
    elif (a != b and a!=c and b == c) or ( a != b and a == c and b!= c ) or ( a == b and a != c and b != c ):
        return ((a+b+c) * (a*a + b*b + c*c))
    elif a==b and a==c and b==c:
        return ((a+b+c) * (a*a + b*b + c*c) * (a*a*a + b*b*b + c*c*c))