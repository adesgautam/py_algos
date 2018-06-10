
# Min-Heap
def heapify(arr, n, i):
	smallest=i
	l = 2*i+1
	r = 2*i+2

	if l<n and arr[l]<arr[i]:
		smallest=l

	if r<n and arr[r]<arr[smallest]:
		smallest=r
	
	if smallest != i:
		arr[i], arr[smallest] = arr[smallest], arr[i]
		heapify(arr, n, smallest)
		
def heap_sort(arr):
	n = len(arr)

	for i in range(n,-1,-1):
		heapify(arr, n, i)

	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]
		print(arr)
		heapify(arr, i, 0)

	return arr

# sort in descending order
# N = input()
# arr = []
# for i in range(int(N)):
# 	arr.append(int(input()))

# for i in range(int(N)):
# 	if i<2:
# 		print(-1)
# 	else:
# 		h = heap_sort(arr[:i+1])
		
# 		h = h[:3]
# 		for i in h:
# 			print(i, end=" ")
# 		print()

arr = [5,6,2,3,4,8,9]
print(heap_sort(arr))







