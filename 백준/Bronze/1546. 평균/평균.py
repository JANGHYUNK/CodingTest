num_count = int(input()) #몇개인지
A = input().split()
real_arr = []
res = 0
#정수로 변환해주고
for i in range(len(A)):
    real_arr.append(int(A[i]))
    
max_num = max(real_arr)

for j in real_arr:
    res += (j/max_num*100)

    
print(res/num_count)