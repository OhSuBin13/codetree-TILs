x, y = 0, 0
cur_dir = 3
#동, 남, 서, 북
dxs, dys = [1,0,-1,0], [0,1,0,-1]
ans = -1
elapse_time = 0

def move(word):
    global x, y, cur_dir, elapse_time
    if word == 'L':
        cur_dir = (cur_dir+3)%4
    elif word == 'R':
        cur_dir = (cur_dir+1)%4
    else:
        x, y = x + dxs[cur_dir], y + dys[cur_dir]
    elapse_time += 1

def is_point(x, y):
    global ans
    if x == 0 and y == 0:
        ans = elapse_time
        return True
    return False

n = input()
for i in n:
    move(i)
    if is_point(x,y):
        break
print(ans)