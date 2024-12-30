alpha = input().strip()  # 사용자 입력
alpha = alpha.upper()  # 대소문자 구분하지 않기 위해 대문자로 변환
alpha_list = list(alpha)  # 리스트로 변환
set_alpha = set(alpha_list)  # 중복 제거

num_count = []
for char in set_alpha:
    count = alpha_list.count(char)  # 해당 문자 개수 세기
    num_count.append((count, char))  # 개수와 문자를 튜플로 저장

num_count.sort(reverse=True, key=lambda x: x[0])  # 개수를 기준으로 내림차순 정렬

# 가장 많이 사용된 알파벳 확인
if len(num_count) > 1 and num_count[0][0] == num_count[1][0]:
    print("?")  # 가장 많이 사용된 알파벳이 여러 개인 경우
else:
    print(num_count[0][1])  # 가장 많이 사용된 알파벳 출력