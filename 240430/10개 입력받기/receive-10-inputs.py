arr = list(map(int, input().split()))
cnt = 0
for elem in arr:
    if elem == 0:
        break
    cnt += 1

sum_val = 0
for i in range (0, cnt, 1):
    sum_val += arr[i]
avg = sum_val / cnt
print(f"{sum_val} {avg:.1f}")