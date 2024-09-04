def solution(s):
    # 문자열을 공백 기준으로 분리
    words = s.split(' ')
    
    result = []
    
    # 각 단어에 대해 반복
    for word in words:
        new_word = ''
        for i in range(len(word)):
            if i % 2 == 0:  # 짝수 인덱스 -> 대문자
                new_word += word[i].upper()
            else:           # 홀수 인덱스 -> 소문자
                new_word += word[i].lower()
        # 변환된 단어를 결과에 추가
        result.append(new_word)
    
    # 공백으로 구분된 단어들을 다시 합침
    return ' '.join(result)


s = "try hello world"
print(solution(s))