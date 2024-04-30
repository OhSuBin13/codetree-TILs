arr = list(map(int, input().split()))
cnt = 0
sum_val = 0
two = []

for elem in arr:
    if elem == 0:
        break
    if elem % 2 == 0:
        two.append(elem)

n = len(two)
sum_val = sum(two)

print(f"{n} {sum_val}")