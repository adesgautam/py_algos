
import numpy as np

# Stack
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


# For directed graphs (see the add_edge() function for undirected graphs)
class Graph:
	def __init__(self):
		self.vertices = []
		self.adj_matrix = np.zeros((0,0), dtype=int)
		self.mapping = {}
		self.rev_mapping = {}
	
	def update(self):
		# update vertices
		for i in range(0,len(self.vertices)):
			self.mapping[self.vertices[i]] = i	
			self.rev_mapping[i] = self.vertices[i]

		# update adj_matrix
		l = len(self.vertices)
		temp = self.adj_matrix
		self.adj_matrix = np.zeros((l,l), dtype=int)
		for i in range(len(temp)):
			self.adj_matrix[i][0:-1] = temp[i]

	def add_vertex(self, v):
		if v not in self.vertices:
			self.vertices.append(v)
		self.update()
	
	def add_edge(self, v1, v2):
		if v1 in self.vertices and v2 in self.vertices:
			# print(self.mapping[v1], self.mapping[v2])
			self.adj_matrix[self.mapping[v1]][self.mapping[v2]] = 1

			# Uncomment the below 3 lines for making adjacency matrix for undirected graphs
			# self.adj_matrix[self.mapping[v2]][self.mapping[v1]] = 1
			# self.adj_matrix[self.mapping[v1]][self.mapping[v1]] = 1
			# self.adj_matrix[self.mapping[v2]][self.mapping[v2]] = 1

	def get_adjacent(self, x):
		i = self.mapping[x]
		adj = []
		# rows
		n=0
		for j in range(len(self.vertices)):
			if self.adj_matrix[i][j] == 1:
				# get vertex name from reverse mapping
				m = self.rev_mapping[j]
				adj.append(m)

		# uncomment below for undirected graphs
		# n=0
		# for j in range(len(self.vertices)):
		# 	if self.adj_matrix[j][i] == 1:
		# 		# get vertex name from reverse mapping
		# 		m = self.rev_mapping[j]
		# 		adj.append(m)

		return adj

	# TODO
	def DFS(self, x):
		visited = {}
		for i in self.vertices:
			visited[i] = False
		s = Stack()
		s.push(x)
		visited[x] = True

		while not s.isEmpty():
			y = s.pop()
			print(y, end=' ')
			adjs = self.get_adjacent(y)
			for i in adjs:
				if visited[i] == False:
					s.push(i)
					visited[i] = True
		

g = Graph()
g.add_vertex('1')
g.add_vertex('2')
g.add_vertex('3')
g.add_vertex('4')
g.add_vertex('5')
g.add_vertex('6')
g.add_vertex('7')

# print vertices added
print(g.vertices)

g.add_edge('1', '2')
g.add_edge('1', '3')
g.add_edge('2', '4')
g.add_edge('2', '5')
g.add_edge('3', '5')
g.add_edge('4', '6')
g.add_edge('5', '6')
g.add_edge('6', '7')

# print adjacency matrix
print(g.adj_matrix)

# Breadh First Search
g.DFS('1')



















