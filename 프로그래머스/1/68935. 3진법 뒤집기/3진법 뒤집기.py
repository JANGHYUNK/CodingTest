def solution(n):
    res = []
    answer = 0

    # 1. n을 3진법으로 변환
    while n > 0:
        res.append(n % 3)  # n을 3으로 나눈 나머지를 리스트에 추가
        n = n // 3         # n을 3으로 나눈 몫으로 업데이트
    
    # 2. 3진법 숫자 뒤집기 (이미 반대로 저장되므로 그대로 둠)
    print("3진법 변환 (뒤집힌 상태):", res)

    # 3. 뒤집힌 3진법을 10진법으로 변환
    for i in range(len(res)):
        answer += res[i] * pow(3, len(res) - i - 1)

    print("10진법 결과:", answer)
    return answer

    

    print(res)

    res.reverse()



    for i in range(len(res)):
        answer += res[i] * pow(3,i)

    print(answer)
    return answer