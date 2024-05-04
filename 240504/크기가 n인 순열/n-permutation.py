n = int(input())
answer = []
visited = [False] * (n+1)
def choose(curr_num):
    for i in range(1, n+1):
        if curr_num == n+1:
            print(*answer)
            return
        if visited[i]:
            continue
        visited[i] = True
        answer.append(i)
        choose(curr_num+1)
        visited[i] = False
        answer.pop()
choose(1)