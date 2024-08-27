def solution(n, m):

    import math
    answer = []
    gcd = math.gcd(n,m)
    answer.append(gcd)

    lcm = n*m //gcd
    answer.append(lcm)

    return answer