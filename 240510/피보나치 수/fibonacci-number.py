n = int(input())

dp = [-1] * (n+1)
def fibbo(n):
    if dp[n] != -1:
        return dp[n]
    if n <= 2:
        dp[n] = 1
    else:
        dp[n] = fibbo(n-1) + fibbo(n-2)
    return dp[n]
fibbo(n)
print(dp[n])