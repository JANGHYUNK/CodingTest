def solution(arr):
    sums = 0
    for i in arr:
        sums += i
    return sums / len(arr)