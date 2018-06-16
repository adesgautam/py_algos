
# Adesh Gautam

def counting_sort(arr, exp):
	c = [0 for _ in range(100)]
	# d = [0 for _ in range(max(arr))]
	d = [0]*len(arr)
	
	# count 
	for i in range(len(arr)):
		t = (arr[i]/exp)%10 
		# print(t)
		c[t] += 1

	for i in range(1,len(c)):
		c[i] += c[i-1]

	for i in range(len(arr)-1,-1,-1):
		t = (arr[i]/exp)%10
		d[c[t] -1] = arr[i]
		c[t] -= 1
	
	return d

def radix_sort(arr):
	m = max(arr)
	i=1
	while (m/i) > 0:
		arr = counting_sort(arr, i)
		i*=10
	return arr

# arr = [1, 4, 1, 2, 7, 5, 2]
arr = [5,4,33,7,1,29,3,6,13]

sorted_array = radix_sort(arr)
print(sorted_array)








