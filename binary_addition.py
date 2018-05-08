
A = '0010'
B = '1011'
C = ''

temp1 = A
temp2 = B
c=0
i=len(A)
while i>=0:
	t1 = temp1[i]
	t2 = temp2[i]

	print(t1,t2)

	if str(t1)==1 and str(t2)==1 and c==0:
		t = 0
		c=1
	else:
		t = (t1 or t2 or c)

	C += str(t) 

	i=i-1

C += str(c)

# for reversing
print(C[::-1])