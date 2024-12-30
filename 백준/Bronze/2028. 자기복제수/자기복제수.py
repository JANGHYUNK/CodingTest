num = int(input())
arr =[input() for i in range(num)]

arr_sqr = []
for i in range(num):
   root = int(arr[i])**2
   arr_sqr.append(str(root))
   
for i in range(num):
    if int(arr[i]) == int(arr_sqr[i][-len(arr[i]):]):
        print("YES")
    else:
        print("NO")