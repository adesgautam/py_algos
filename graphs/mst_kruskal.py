
import numpy as np

# For directed graphs (see the add_edge() function for undirected graphs)
class Graph:
	def __init__(self):
		self.vertices = []
		self.weight_vertex = []
		# self.mapping = {}

	def add_vertex(self, v):
		if v not in self.vertices:
			self.vertices.append(v)
	
	def add_edge(self, src, dest, weight):
		if src in self.vertices and dest in self.vertices:
			wsd = [weight, src, dest]
			self.weight_vertex.append(wsd)

def sort(wsd):
	for i in range(len(wsd)):
	    for j in range(len(wsd)):
	        if wsd[i][0] < wsd[j][0]:
	            wsd[i], wsd[j] = wsd[j], wsd[i]
	return wsd

def check_cycle(vertex_pairs, wsd):
	s, d = wsd[1], wsd[2]
	b = cycle_helper(vertex_pairs, s, d)
	return b

def cycle_helper(vertex_pairs, s, d):
	if vertex_pairs == []:
		# return False
		print("empty")
	else:
		s1, c = s, 0
		for i in vertex_pairs:
			if i==vertex_pairs[1] or i==vertex_pairs[2]:
				c+=1
		t = []
		for i in range(c):
			for j in vertex_pairs:
				# while d != s1:
				print(s1, j[0], j[1])
				if s1 == j[0]:
					s1 = j[1]
				elif s1 == j[1]:
					s1 = j[0]
				else:
					if s1 != d:
						s1 = s
						t.append(False)
		print(t)


g = Graph()
g.add_vertex('0')
g.add_vertex('1')
g.add_vertex('2')
g.add_vertex('3')
g.add_vertex('4')
g.add_vertex('5')
g.add_vertex('6')
g.add_vertex('7')
g.add_vertex('8')

# print vertices added
print(g.vertices)

g.add_edge('0', '1', 4)
g.add_edge('0', '7', 8)
g.add_edge('1', '2', 8)
g.add_edge('1', '7', 11)
g.add_edge('2', '3', 7)
g.add_edge('2', '8', 2)
g.add_edge('2', '5', 4)
g.add_edge('3', '4', 9)
g.add_edge('3', '5', 14)
g.add_edge('4', '5', 10)
g.add_edge('5', '6', 2)
g.add_edge('6', '8', 6)
g.add_edge('6', '7', 1)
g.add_edge('8', '7', 7)


# print weight, src, dest
# print(["Weight", "Src", "Dest"])
# for i in g.weight_vertex:
# 	print(i)

# First sort according to the weights
wsd = sort(g.weight_vertex)
# for i in wsd:
# 	print(i)

vertex_pairs = []
# for i in wsd:
# 	chk = check_cycle(vertex_pairs, i)
for i in range(5):
	vertex_pairs.append([g.weight_vertex[i][1], g.weight_vertex[i][2]])

print('\n', vertex_pairs)
cycle_helper(vertex_pairs, '6', '8')






















