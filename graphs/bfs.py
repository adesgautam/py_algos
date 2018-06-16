import numpy as np

# Queue
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
			x = self.items[self.head]
			self.items.pop(self.head)
			return x

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)


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
	def BFS(self, x):
		visited = {}
		for i in self.vertices:
			visited[i] = False
		q = Queue()
		q.enqueue(x)

		visited[x] = True

		while not q.isEmpty():
			y = q.dequeue()
			print(y, end=' ') 
			# get adjacent nodes
			adj = self.get_adjacent(y)
			
			for i in adj:
				if visited[i] == False:
					q.enqueue(i)
					visited[i] = True


g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('E')

# print vertices added
print(g.vertices)

g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.add_edge('A', 'C')
g.add_edge('B', 'E')
g.add_edge('C', 'D')
g.add_edge('D', 'C')
g.add_edge('E', 'A')

# print adjacency matrix
print(g.adj_matrix)

# Breadh First Search
g.BFS('A')



















