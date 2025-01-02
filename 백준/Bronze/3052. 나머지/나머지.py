mod_arr = []
for _ in range(10):
    mod_arr.append(int(input())%42)

mod_arr = set(mod_arr)
print(len(mod_arr))