import sys

N = int(input().strip())  # 공백 제거
arr = []

for i in range(N):
    arr.append(int(sys.stdin.readline().strip()))  # 입력값 공백 제거
    
arr.sort()
for i in arr:
    print(i)
