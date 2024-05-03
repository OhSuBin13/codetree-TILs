n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range (n)
]

res = 0
def in_range(x, y):
    return x >= 0 and x < n-2 and y >= 0 and y < n-2

def check_coin(x, y):
    cnt = 0
    for i in range(x, x+3):
        for j in range(y, y+3):
            if arr[i][j] == 1:
                cnt += 1
    return cnt
for i in range(n):
    for j in range(n):
        if not in_range(i,j):
            continue
        coin = check_coin(i,j)
        res = max(coin, res)
print(res)