n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]
    
def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def can_go(x,y):
    if not in_range(x,y):
        return False
    elif grid[x][y] == 0:
        return False
    elif visited[x][y]:
        return False
    return True

def dfs(x,y):
    dxs, dys = [1,0], [0,1]
    for dx, dy in zip(dxs, dys):
        new_x = x + dx
        new_y = y + dy

        if not can_go(new_x, new_y):
            continue
        visited[new_x][new_y] = 1
        dfs(new_x, new_y)

visited[0][0] = 1
dfs(0, 0)
print(visited[n-1][m-1])