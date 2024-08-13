def solution(s):
    sorted_string = ''.join(sorted(s, reverse=True))
    return sorted_string