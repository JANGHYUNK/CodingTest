def solution(phone_number):
    answer = '*'
    return (answer * (len(phone_number)-4)) + phone_number[-4:-1] + phone_number[-1]