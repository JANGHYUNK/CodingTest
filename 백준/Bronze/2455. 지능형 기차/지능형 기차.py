arr = []
res = []
for i in range(4):
    N, M = map(int, input().split())
    arr.append(M-N)

res.append(arr[0])
res.append(res[0] + arr[1])
res.append(res[1] + arr[2])
res.append(res[2] + arr[3])
print(max(res))