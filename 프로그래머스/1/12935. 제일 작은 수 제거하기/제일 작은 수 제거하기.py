def solution(arr):       
    arr_min = min(arr)
    arr_index = arr.index(arr_min)
    del arr[arr_index]

    if arr == []:
        arr.append(-1)
        return arr
    else:
        return arr