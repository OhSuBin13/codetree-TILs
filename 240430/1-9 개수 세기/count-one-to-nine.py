n = int(input())
cnt_arr = [0] * 10
arr = list(map(int, input().split()))

for elem in arr:
    cnt_arr[elem] += 1
    
for i in range(1,10):
    print(cnt_arr[i])