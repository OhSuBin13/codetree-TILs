#동,남,서,북
dxs, dys = [1,0,-1,0], [0,-1,0,1]
n = int(input())
res = 0
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x,y):
    return x >= 0 and x < n and y >= 0 and y < n

for x in range(n):
    for y in range(n):
        cnt = 0;
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx,ny) and arr[nx][ny] == 1:
                cnt +=1
        if cnt >= 3:
            res += 1

print(res)