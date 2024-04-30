cnt_arr = [0] * 5

for _ in range(3):
    s, t = input().split()
    t = int(t)

    if(t >= 37 and s == 'Y'):
        cnt_arr[1] += 1
    elif(t >= 37):
        cnt_arr[2] += 1
    elif(t < 37 and s == 'Y'):
        cnt_arr[3] += 1
    else:
        cnt_arr[4] += 1

for i in range(1,5):
    print(cnt_arr[i], end = " ")

if cnt_arr[1] >= 2:
    print("E")