arr = list(map(int, input().split()))
for i in range(2, 10):
    arr.append((arr[i-1] + arr[i-2]) % 10)

for i in range(0, 10):
    print(arr[i], end = " ")