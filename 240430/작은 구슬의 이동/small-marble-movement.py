n, t = tuple(map(int, input().split()))
x,y,c_dir = input().split()
x = int(x)
y = int(y)

d = {
    'R':0,
    'D':1,
    'U':2,
    'L':3
}

dxs, dys = [0,1,-1,0], [1,0,0,-1]
x,y,move_dir = x-1, y-1, d[c_dir]

def in_range(x,y):
    return x>=0 and x < n and y>=0 and y < n

for _ in range(t):
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    if in_range(nx,ny):
        x, y = nx, ny
    else:
        move_dir = 3-move_dir
print(x+1,y+1)