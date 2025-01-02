num = int(input())
arr = []
for i in range(num):
    numbers,eng = input().split()
    numbers = int(numbers)
    
    result = ''.join([R*numbers for R in eng])
    arr.append(result)

for j in arr:
    print(j)