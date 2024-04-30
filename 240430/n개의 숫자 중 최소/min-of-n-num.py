n = int(input())
arr = list(map(int, input().split()))
max_val = arr[0]
min_val = arr[0]

for elem in arr[1:]:
    if elem < min_val:
        min_val = elem
    if elem > max_val:
        max_val = elem

cnt = 0
for elem in arr:
    if elem == min_val:
        cnt +=1

print(f"{min_val} {cnt}")