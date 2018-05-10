
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
			print(self.head)
			self.items.pop(self.head)

	def isEmpty(self):
		return self.head == self.tail

	def size(self):
		return len(self.items)

q = Queue()
print(q.isEmpty())
# insert
for i in range(1,6):
	q.enqueue(i)

# check
print(q.items, q.head, q.tail)
print(q.size())
print(q.isEmpty())

# remove
q.dequeue()
# check
print(q.items, q.head, q.tail)

# remove
q.dequeue()
# check
print(q.items, q.head, q.tail)
	







