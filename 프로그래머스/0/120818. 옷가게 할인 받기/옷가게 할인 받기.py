def solution(price):
    if 300000 > price >= 100000:
        result = price * 0.95
        return int(result)
    elif 500000 > price >= 300000:
        result = price * 0.90
        return int(result)
    elif price >= 500000:
        result = price * 0.80
        return int(result)
    else:
        return int(price)