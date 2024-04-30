dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
x, y = 0, 0
n = int(input())

for i in range(n):
    name, dir_num = input().split()
    dir_num = int(dir_num)
    if name == 'E':
        move_dir = 0
    elif name == 'W':
        move_dir = 1
    elif name == 'S':
        move_dir = 2
    else:
        move_dir = 3
    x += dx[move_dir] * dir_num
    y += dy[move_dir] * dir_num
print(f"{x} {y}")