
# N = input()
# arr = input().split()
# arr = [int(i) for i in arr]
# arr = arr[:int(N)]
arr = [5,6,2,3,4,8,9]
swaps=0
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i]>arr[j]:
            swaps+=1
            arr[i], arr[j] = arr[j], arr[i]
       

print(arr, swaps)