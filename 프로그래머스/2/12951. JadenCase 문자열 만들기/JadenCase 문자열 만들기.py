def solution(s):
    # 먼저 주어진 문자열을 공백 기준으로 split하여 각 단어로 나눕니다.
    words = s.split(' ')
    res = []

    for word in words:
        # 빈 문자열(연속된 공백으로 인해 생성된 경우)은 그대로 추가합니다.
        if word == "":
            res.append("")
        else:
            # 첫 문자가 알파벳인 경우
            if word[0].isalpha():
                # 첫 문자는 대문자로, 나머지는 소문자로 변환
                res.append(word[0].upper() + word[1:].lower())
            else:
                # 첫 문자가 알파벳이 아닌 경우, 첫 문자는 그대로 두고 나머지는 소문자로 변환
                res.append(word[0] + word[1:].lower())
  
    # 원래 문자열의 공백을 유지하기 위해 ' '로 join하여 반환
    return ' '.join(res)
