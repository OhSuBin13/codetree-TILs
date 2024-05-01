n, m = tuple(map(int, input().split()))
arr = [
    [0] * n
    for _ in range(n)
]
dxs, dys = [1,0,-1,0], [0,1,0,-1]

def in_range(x,y):
    if x >= 0 and x < n and y >=0 and y < n:
        return True
    return False

def count(x,y):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and arr[nx][ny] == 1:
            cnt += 1
    
    return cnt

for i in range(m):
    a, b = tuple(map(int, input().split()))
    a -= 1
    b -= 1
    arr[a][b] = 1
    if count(a,b) == 3:
        print('1')
    else:
        print('0')