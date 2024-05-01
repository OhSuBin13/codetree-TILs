n = int(input())
arr =[
    [0] * n
    for _ in range(n)
]
x, y = n // 2, n // 2
arr[x][y] = 1

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def move(x, y):
    dxs, dys = [0,-1,0,1], [1,0,-1,0]
    for i in range (2,n*n+1):
        for j in range(4):
            nx, ny = x + dxs[j], y + dys[j]
            if in_range(nx, ny) and arr[nx][ny] == 0:
                x, y = nx, ny
                arr[nx][ny] = i
                break

move(x,y)
for i in range(n):
    for j in range(n):
        print(arr[i][j], end = " ")
    print()