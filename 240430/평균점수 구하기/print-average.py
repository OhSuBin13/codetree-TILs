arr = list(map(float, input().split()))
sum_val = sum(arr)
n = len(arr)
avg = sum_val / n

print(f"{avg:.1f}")