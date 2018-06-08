
import numpy as np

# Recursive
def LCS_rec(str1, str2, l1, l2):
	if l1==0 or l2==0:
		return 0
	elif str1[l1-1] == str2[l2-1]:
		return 1+ LCS_rec(str1, str2, l1-1, l2-1)
	else:
		return max(LCS_rec(str1, str2, l1, l2-1), LCS_rec(str1, str2, l1-1, l2))

# Optimal
def LCS_opt(str1, str2, l1, l2):
	L = np.zeros((l1+1, l2+1), dtype=np.int)
	match = []
	for i in range(l1+1):
		for j in range(l2+1):
			if i==0 or j==0:
				L[i][j] = 0
			elif str1[i-1] == str2[j-1]:
				L[i][j] = 1 + L[i-1][j-1]
			else:
				L[i][j] = max(L[i-1][j], L[i][j-1])
	print(L)
	
	match = []
	i,j = l1-1,l2-1
	while i!=0 and j!=0:
		if str1[i] != str2[j]:
			if L[i-1][j] > L[i][j-1]:
				i=i-1
			else:
				j=j-1
		else:
			match.append(str1[i])
			i=i-1
			j=j-1
	match.append(str1[0])
	return L[l1][l2], match[::-1]

str1 = "ABSJABHWQ"
str2 = "ABHWQAAA"
l1 = len(str1)
l2 = len(str2)

length1 = LCS_rec(str1, str2, l1, l2)
length2, match = LCS_opt(str1, str2, l1, l2)

print(length2)
print(''.join(match))






