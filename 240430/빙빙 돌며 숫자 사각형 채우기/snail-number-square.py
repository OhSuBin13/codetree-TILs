n, m = tuple(map(int, input().split()))
answer =[
    [0] * m
    for _ in range(n)
]
x, y = 0,0
answer[x][y] = 1
#R,D,L,U
dxs, dys = [0,1,0,-1], [1,0,-1,0]
c_dir = 0

def in_range(x,y):
    return x>=0 and x<n and y >=0 and y < m

for i in range(2, n * m + 1):
    nx, ny = x + dxs[c_dir], y + dys[c_dir]
    if not in_range(nx,ny) or answer[nx][ny] != 0:
        c_dir = (c_dir+1) % 4
    x, y = x + dxs[c_dir], y+ dys[c_dir]    
    answer[x][y] = i

for i in range(n):
    for j in range(m):
        print(answer[i][j], end = " ")
    print()