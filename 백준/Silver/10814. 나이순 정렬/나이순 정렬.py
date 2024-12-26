N = int(input())  # 회원 수 입력
members = []

for i in range(N):
    age, name = input().split()
    age = int(age)  # 나이를 정수로 변환
    members.append((age, name,i))  # 나이, 이름, 가입 순서 (i)를 저장

# 나이를 기준으로 오름차순 정렬하고, 나이가 같으면 가입 순서대로 정렬
members.sort(key=lambda x: (x[0], x[2]))

# 결과 출력
for member in members:
    print(member[0], member[1])