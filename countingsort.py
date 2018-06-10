
# Adesh Gautam

def counting_sort(arr):
	c = [0 for _ in range(10)]
	d = [0 for _ in range(max(arr))]
	
	# count 
	for i in range(len(arr)):
		c[arr[i]] += 1

	for i in range(1,len(c)):
		c[i] += c[i-1]

	for i in range(len(arr)):
		d[c[arr[i]]-1] = arr[i]
		c[arr[i]] -= 1
	
	return d

# arr = [1, 4, 1, 2, 7, 5, 2]
arr = [5,4,3,7,1,9,3,6,3]

sorted_array = counting_sort(arr)
print(sorted_array)








