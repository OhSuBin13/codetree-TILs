k, n = tuple(map(int, input().split()))
answer = []

def choose(curr_num):
    if curr_num == n+1:
        print(*answer)
        return
    
    for i in range(1, k+1):
        if curr_num >= 3 and i == answer[-1] and i == answer[-2]:
            continue
        answer.append(i)
        choose(curr_num+1)
        answer.pop()
choose(1)