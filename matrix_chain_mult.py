import sys
import numpy as np

# non-dynamic O(2^n)
def matrix_chain_order(arr, i, j):
	if i==j:
		return 0
	min = sys.maxsize
	for k in range(i,j):
		val = matrix_chain_order(arr, i, k) + matrix_chain_order(arr, k+1, j) + arr[i-1]*arr[k]*arr[j]
		if val < min:
			min = val

	return min

# using dynamic programming
def matrix_chain_order(arr):
	n = len(arr)
	m = [[0 for _ in range(n)] for _ in range(n)]

	for l in range(2,n):
		for i in range(1,n-l+1):
			j = i+l-1
			m[i][j] = 9999
			for k in range(i,j):
				val = m[i][k] + m[k+1][j] + arr[i-1]*arr[k]*arr[j]
				if val < m[i][j]:
					m[i][j] = val
	return m[1][n-1]


mat_dims = [1, 2, 3, 4]
l = len(mat_dims)

# min_mults = matrix_chain(mat_dims, 1, l-1)
# print("Minimum multiplications needed: ", min_mults)


m = matrix_chain_order(mat_dims)
print(m)








