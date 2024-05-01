n = int(input())
arr = [
    input()
    for _ in range(n)
]
start_point = int(input())

def init(num):
    if num <= n:
        return 0, num-1, 0
    elif num <= 2*n:
        return num-n-1, n-1, 1
    elif num <= 3*n:
        return n-1, n-(num-2*n), 2
    else:
        return n-(num-3*n), 0, 3
    
def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def move(x, y, next_dir):
    dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]
    nx, ny = x + dxs[next_dir], y + dys[next_dir]
    return nx, ny, next_dir

def simulate(x, y, move_dir):
    move_num = 0
    while in_range(x, y):
        # 0 <-> 1 / 2 <-> 3
        if arr[x][y] == '/':
            x, y, move_dir = move(x, y, move_dir ^ 1)
        # 0 <-> 3 / 1 <-> 2
        else:
            x, y, move_dir = move(x, y, 3 - move_dir)
        
        move_num += 1
    
    return move_num

x, y, cur_dir = init(start_point)
result = simulate(x, y, cur_dir)
print(result)