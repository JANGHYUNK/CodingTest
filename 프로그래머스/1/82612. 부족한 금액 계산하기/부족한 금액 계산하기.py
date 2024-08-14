def solution(price, money, count):
    price_res  =0
    
    for i in range(1,count+1):
        price_res += price * i  

    if money >= price_res:
        return 0
    else:
        return price_res - money  

    return answer