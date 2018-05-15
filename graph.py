import numpy as np

# For directed graphs (see the add_edge() function for undirected graphs)
class Graph:
	def __init__(self):
		self.vertices = []
		self.adj_matrix = np.zeros((0,0), dtype=int)
		self.mapping = {}
	
	def update(self):
		# update vertices
		for i in range(0,len(self.vertices)):
			self.mapping[self.vertices[i]] = i	

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








