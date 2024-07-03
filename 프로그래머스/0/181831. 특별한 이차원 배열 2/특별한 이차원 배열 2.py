def solution(arr):
    for i,k in enumerate(arr):
        for j, v in enumerate(k):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1
                   
                