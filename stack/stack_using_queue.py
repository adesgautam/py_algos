
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
			return None
		else:
			x = self.items[self.head]
			self.items.pop(self.head)
			return x

	def isEmpty(self):
		return self.head == self.tail

	def size(self):
		return len(self.items)


class Stack:
	def __init__(self):
		self.q1 = Queue()
		self.size = 0
		self.items = []

	def push(self, x):
		self.q1.enqueue(x)
		self.size+=1
		self.items = self.q1.items
		
	def pop(self):
		for _ in range(len(self.q1.items)-1):
			self.q1.enqueue(self.q1.dequeue())
		self.q1.dequeue()
		# self.items = self.q1.items

	def size(self):
		return self.size

	def isempty(self):
		return self.q1.isEmpty()

s = Stack()
for i in range(1,7):
	s.push(i)
print(s.items)
s.pop()
print(s.items)



