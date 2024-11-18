def sum_of_digits(serial):
    # 시리얼 번호에서 숫자들의 합을 구하는 함수
    return sum(int(ch) for ch in serial if ch.isdigit())

def custom_key(serial):
    # 길이, 숫자 합, 사전 순으로 정렬하는 key 생성
    return (len(serial), sum_of_digits(serial), serial)

# 시리얼 번호 입력 받기
num = int(input())
serial_numbers = [input().strip() for _ in range(num)]

# 시리얼 번호를 정렬
serial_numbers.sort(key=custom_key)

# 정렬된 결과 출력
for serial in serial_numbers:
    print(serial)