
N = input()
arr = input().split()
arr = arr[:int(N)]
arr = [int(i) for i in arr]
arr.sort()

qn = input()
q=[]
for _ in range(int(qn)):
	t = input()
	q.append(int(t))

print("q: ",q)

def bin_search(val):
	low=0
	high = len(arr)-1

	while low<=high:
		mid = int(low + (high-low)/2)
		if val == arr[mid]:
			print(mid)
			return mid+1
		elif val>arr[mid]:
			low=mid+1
		else :
			high=mid-1
		
	return -1


for i in q:
	j = bin_search(i)
	print(j)







