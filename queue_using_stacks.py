

class Stack:
	def __init__(self):
		self.items = []
		self.head = -1

	def push(self, x):		
		self.head+=1
		self.items.insert(self.head, x)		

	def pop(self):
		if self.isEmpty():
			print("Stack is empty !!!")
		else:
			x = self.items[self.head]
			self.items.pop(self.head)
			self.head-=1
			return x

	def size(self):
		return len(self.items)

	def isEmpty(self):
		return self.head == -1


class Queue:
	def __init__(self):
		self.s1, self.s2 = Stack(), Stack()
		self.head = 0
		self.tail = 0
		self.size = 0
		self.items = []

	def enqueue(self, x):
		self.s1.push(x)
		self.size+=1
		self.items = self.s1.items

	def dequeue(self):
		if self.s1.isEmpty():
			print("Queue is Empty !!!")
		else:
			# print(self.s1.items)
			for _ in range(len(self.s1.items)):
				self.s2.push(self.s1.pop())
			self.s2.pop()
			for _ in range(len(self.s2.items)):
				self.s1.push(self.s2.pop())
			self.items = self.s1.items

	def size(self):
		return self.size

	def isEmpty(self):
		return self.s1.isEmpty()

q = Queue()
for i in range(1,6):
	q.enqueue(i)
print(q.items)

q.dequeue()
print(q.items)



