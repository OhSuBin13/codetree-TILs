x, y = 0, 0
#동, 남, 서, 북
dxs, dys = [1,0,-1,0], [0, 1, 0, -1]
n = int(input())
time = 0
for _ in range(n):
    cur_dir, dist = input().split()
    dist = int(dist)
    if cur_dir == 'E':
        direction = 0
    elif cur_dir == 'S':
        direction = 1
    elif cur_dir == 'W':
        direction = 2
    else:
        direction = 3
    for i in range(dist):
        x, y = x + dxs[direction], y + dys[direction]
        time += 1
        if x == 0 and y == 0:
            break
            
    if x == 0 and y == 0:
        break
print(time)