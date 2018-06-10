class Queue:
	def __init__(self):
		self.items = []
		self.head = 0
		self.tail = 0

	def enqueue(self, x):
		self.items.insert(self.tail, x)
		self.tail+=1

	def dequeue(self):
		if self.isEmpty():
			print("Queue is empty !!!")
		else:
			self.items.pop(self.head)
			# self.head+=1

	def isEmpty(self):
		return self.head == self.tail

	def size(self):
		return len(self.items)

# Method 1 (Making push costly)
class Stack:
	def __init__(self):
		self.q1, self.q2 = Queue(), Queue()
		self.size = 0
		self.items = []

	def push(self, x):
		# pushing x in to q2
		self.q2.enqueue(x)
		self.size+=1

		# pushing every item from q1 to q2
		for i in self.q1.items:
			self.q2.enqueue(i)
		
		self.q1.items = []
		# interchanging q1 and q2
		self.q1, self.q2 = self.q2, self.q1
		self.items = self.q1.items
		
	def pop(self):
		if self.q1.isEmpty():
			print("Stack is empty !!!")
		else:
			self.q1.dequeue()
			self.size-=1
		

	def size(self):
		return self.size

	def isEmpty(self):
		return self.q1.isEmpty()

# Method 2 (Making pop costly)
class Stack1:
	def __init__(self):
		self.q1, self.q2 = Queue(), Queue()
		self.size = 0
		self.items = []

	def push(self, x):
		self.q1.enqueue(x)
		self.size+=1
		self.items = self.q1.items
		
	def pop(self):
		if self.q1.isEmpty():
			print("Stack is empty !!!")
		else:
			l = len(self.q1.items)
			for i in range(l-1):
				self.q2.enqueue(self.q1.items[i])
			self.q1.items = []
			self.size-=1

			self.q1, self.q2 = self.q2, self.q1
			self.items = self.q1.items

	def size(self):
		return self.size

	def isEmpty(self):
		return self.q1.isEmpty()

s = Stack1()
for i in range(1,7):
	s.push(i)
print(s.items)
print(s.size)
s.pop()
s.pop()
print(s.items)







