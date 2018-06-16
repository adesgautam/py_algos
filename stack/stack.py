
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

s = Stack()
x = s.pop()
for i in range(1,6):
	s.push(i)
print(s.items, s.head)
x = s.pop()
print(s.items)
print(s.isEmpty())
print(s.size())






