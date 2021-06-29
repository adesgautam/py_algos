
# Insertion sort
arr = [7, 1, 3, 2, 4, 5, 6]

def insertion_sort(arr):
	for j in range(1,len(arr)):
		key = arr[j]
		# print(arr, j)
		i=j-1
		while i>=0 and arr[i]>key:
			arr[i+1]=arr[i]
			i=i-1
			# print(arr)
		arr[i+1] = key
	return arr

print("Insertion Sort: ", insertion_sort(arr))

# Binary insertion sort
def binary_search(arr, val, start, end):

	if start==end:
		if arr[start]>val:
			return start
		else:
			return start+1

	if start>end:
		return start

	mid = (start+end)/2
	if val > arr[mid]:
		return binary_search(arr, val, mid+1, end)
	elif val< arr[mid]:
		return binary_search(arr, val, start, mid-1)
	else:
		return mid+1

def binary_insertion_sort(arr):
	for i in range(len(arr)):
		val = arr[i]
		j = binary_search(arr, val, 0, i-1)
		# print(j, i, arr[:j], val, arr[j:i], arr[i+1:])
		arr = arr[:j]+[val]+arr[j:i]+arr[i+1:]

	return arr

arr1 = [5,2,4,6,1,3]
print("Binary Insertion Sort: ", binary_insertion_sort(arr1))



