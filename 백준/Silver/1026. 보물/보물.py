# 입력 받기
N = int(input())  # 배열의 길이
A = list(map(int, input().split()))  # 배열 A
B = list(map(int, input().split()))  # 배열 B

# 배열 정렬
A.sort()  # A는 오름차순
B.sort(reverse=True)  # B는 내림차순

# S 값 계산
S = sum(A[i] * B[i] for i in range(N))

# 결과 출력
print(S)
