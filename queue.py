
class Queue:
	def __init__(self):
		self.items = []
		self.head = -1
		self.tail = -1

	def enqueue(self, x):
		self.tail+=1
		self.items.insert(self.tail, x)

	def dequeue(self):
		if self.isEmpty():
			print("Queue is empty !!!")
		else:
			self.items.remove(self.items[self.head])
			self.head-=1

	def isEmpty(self):
		return self.head == self.tail

	def size(self):
		return len(self.items)

q = Queue()
print(q.isEmpty())
for i in range(1,6):
	q.enqueue(i)
print(q.items, q.head, q.tail)
print(q.size())
print(q.isEmpty())
q.dequeue()
print(q.items)
	







