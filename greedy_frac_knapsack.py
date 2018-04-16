
# Adesh Gautam

def quicksort(arr, low, high):
	if low<high:
		pi = partition(arr, low, high)
		quicksort(arr, low, pi-1)
		quicksort(arr, pi+1, high)


def partition(arr, low , high):
	pivot = arr[high]
	i=low-1

	for j in range(low, high):
		if arr[j]>=pivot:
			i+=1
			arr[i], arr[j] = arr[j], arr[i]
			w[i], w[j] = w[j], w[i]
			p[i], p[j] = p[j], p[i]

	arr[high], arr[i+1] = arr[i+1], arr[high]
	w[high], w[i+1] = w[i+1], w[high]
	p[high], p[i+1] = p[i+1], p[high]
	return i+1


W = 60
w = [40, 10, 20, 24]
p = [280, 100, 120, 120]

ratio = [ j/i for i,j in zip(w,p) ]
print("Weights: {0}".format(w))
print("Profits: {0}".format(p))
print("Ratios: {0}\n".format(ratio))

quicksort(ratio,0,3)
print("Sorted Ratios: {0}".format(ratio))
print("Sorted Weights: {0}".format(w))
print("Sorted Profits: {0}".format(p))

profit=0
W1=0
for i in range(0,4):
	print(profit)
	if W1+w[i] <= W:
		profit = profit+p[i]*1
		W1 = W1+w[i]
	else:
		profit = profit+p[i] * ((W-W1)/w[i])
		W1=W
		break

print("Profit: {0}".format(profit))




