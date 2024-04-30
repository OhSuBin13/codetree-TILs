a, b = input().split()
a = int(a)
b = int(b)
cnt_arr = [0] * b

while a > 1:
    cnt_arr[a % b] += 1
    a = a // b

sum_val = 0
for i in range(0, b):
    sum_val += cnt_arr[i] ** 2
print(sum_val)