n, m = tuple(map(int,input().split()))
answer = []
def choose(cur_num, cnt):
    if(cur_num == n+1):
        if cnt == m:
            print(*answer)
        return
    answer.append(cur_num)
    choose(cur_num+1, cnt+1)
    answer.pop()

    choose(cur_num+1,cnt)
choose(1,0)