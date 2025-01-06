num = int(input())
nums = [int(input()) for _ in range(num)]
nums.sort()

for num in nums:
    print(num)