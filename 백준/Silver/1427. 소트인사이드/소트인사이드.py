num = input()
num = list(map(int,num))
num.sort(reverse=True)
S= ""
for i in range(len(num)):
    S += str(num[i])
print(int(S))