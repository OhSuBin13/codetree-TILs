dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
x, y = 0, 0
move = input()
move_dir = 3

for name in move:
    if name == 'L':
        move_dir = (move_dir-1+4) % 4
    elif name == 'R':
        move_dir = (move_dir+1) %4
    elif name == 'F':
        x += dx[move_dir]
        y += dy[move_dir]
print(f"{x} {y}")