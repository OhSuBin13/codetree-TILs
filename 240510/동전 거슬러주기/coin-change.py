n, m = tuple(map(int, input().split()))
coin = list(map(int, input().split()))
max_ans = 10001
dp = [max_ans for _ in range(m+1)]
dp[0] = 0

for i in range(1, m+1):
    for j in range(n):
        if i >= coin[j] and dp[i-coin[j]] != -1:
            dp[i] = min(dp[i], dp[i-coin[j]] + 1)

print(dp[m])