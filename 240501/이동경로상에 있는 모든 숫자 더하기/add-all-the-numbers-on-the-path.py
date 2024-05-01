n, t = tuple(map(int, input().split()))
command = input()
arr = [
    input().split()
    for _ in range(n)
]
cur_dir = 0
x, y = n // 2, n // 2
#북,서,남,동
dxs, dys = [-1,0,1,0], [0,-1,0,1]
result = 0
result += int(arr[x][y])

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

for elem in command:
    if elem == 'L':
        cur_dir = (cur_dir+1) % 4
    elif elem == 'R':
        cur_dir = (cur_dir+3) % 4
    else:
        nx, ny = x + dxs[cur_dir], y + dys[cur_dir]
        if in_range(nx,ny):
            x, y = nx, ny
            result += int(arr[x][y])

print(result)