#분수합 - 최대공약수로 나눌것
import math      

A = list(map(int,input().split())) 
B = list(map(int,input().split())) 
res = []
res.append(A[0]*B[1] + B[0]*A[1])
res.append(A[1]*B[1])

gcd_num = math.gcd(res[0],res[1])

res[0] = res[0] // gcd_num
res[1] = res[1] // gcd_num

for i in res:
    print(i, end=" ")