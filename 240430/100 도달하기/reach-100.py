n = int(input())
arr = []
arr.append(1)
arr.append(n)

for i in range(2, 20):
    new_arr = arr[i-1] + arr[i-2]
    arr.append(new_arr)
    if(new_arr >= 100):
        break

for elem in arr:
    print(elem, end = " ")