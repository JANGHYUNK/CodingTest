import sys

N = int(sys.stdin.readline().strip()) 

# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (10000+1)

for i in range(N):
    array = int(sys.stdin.readline())
    count[array] += 1 # 각 데이터에 해당하는 인덱스의 값 증가
    
for i in range(len(count)): #리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i)  
    