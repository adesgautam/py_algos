# Write your code here
l1 = input().split()
N, M = int(l1[0]), int(l1[1])

arr = input().split()
arr = arr[:N]
res=0
for i in range(len(arr)-1,0,-1):
    if M == int(arr[i]):
        res=i
        break

print(res+1)