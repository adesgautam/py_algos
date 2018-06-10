
# Adesh Gautam

import numpy as np

def quicksort(arr, low, high):
	if low<high:
		pi = partition(arr, low, high)
		quicksort(arr, low, pi-1)
		quicksort(arr, pi+1, high)


def partition(arr, low , high):
	pivot = arr[high]
	i=low-1

	for j in range(low, high):
		if arr[j]<=pivot:
			i+=1
			arr[i], arr[j] = arr[j], arr[i]

	arr[high], arr[i+1] = arr[i+1], arr[high]
	return i+1

# Randomized Quick Sort
def randomized_partition(arr, low, high):
	x = np.random.randint(low, high)
	arr[high], arr[x] = arr[x], arr[high]
	return partition(arr, low, high)

def randomized_quicksort(arr, low, high):
	if low<high:
		x = randomized_partition(arr, low, high)
		randomized_quicksort(arr, low, x-1)
		randomized_quicksort(arr, x+1, high)

arr = [3,5,8,2,5,9,3,10]
# quicksort(arr, 0, 7)
randomized_quicksort(arr, 0, 7)
print(arr)






