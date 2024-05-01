n, m = tuple(map(int, input().split()))
arr = [
    [0] * m
    for _ in range(n)
]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def move(x,y,cur_dir):
    #남,동,북,서
    dxs, dys = [1,0,-1,0], [0,1,0,-1]
    for i in range(n*m):
        nx, ny = x + dxs[cur_dir], y + dys[cur_dir]
        if not in_range(nx, ny) or arr[nx][ny] != 0:
            cur_dir = (cur_dir+1) % 4
        arr[x][y] = i+1
        x, y = x + dxs[cur_dir], y + dys[cur_dir]

move(0,0,0)
for i in range(n):
    for j in range(m):
        print(arr[i][j], end = " ")
    print()