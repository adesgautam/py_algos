
class Stack:
	def __init__(self):
		self.items = []

	def push(self, x):
		self.items.append(x)

	def pop(self):
		self.items.pop()

	def size(self):
		return len(self.items)

	def isEmpty(self):
		return self.items == []

s = Stack()
for i in range(1,6):
	s.push(i)
print(s.items)
s.pop()
print(s.items)
print(s.isEmpty())
print(s.size())






