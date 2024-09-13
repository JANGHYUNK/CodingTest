num = int(input())
list_s = []
for i in range(num):
    p = input()
    list_s.append(p)

lst = set(list_s)
list_s = list(lst)
list_s.sort()
list_s.sort(key = len)

for i in list_s:
    print(i)