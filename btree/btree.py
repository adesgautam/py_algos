

class BTreeNode():
	def __init__(self, leaf):
		self.keys = []
		self.num_keys = len(self.keys)
		self.children = []
		self.is_leaf = leaf

	def __str__(self):
		if self.is_leaf:
			print("Leaf Node with {0} keys, {1} children.\n KEYS: {2}\nCHILDREN: {3}".format(self.num_keys, len(self.children), self.keys, self.children))
		else:
			print("Internal Node with {0} keys, {1} children.\n KEYS: {2}\nCHILDREN: {3}".format(self.num_keys, len(self.children), self.keys, self.children))

class BTree():

	def __init__(self):
		self.root = BTreeNode(leaf=False)
		self.t = t

	def search(self, node=self.root, key):
		i=0
		while i <= x.num_keys and k > x.keys[i]:
			i+=1
		if i<= x.num_keys and k == x.keys[i]:
			return x, i
		elif x.is_leaf:
			return None
		else:
			self.self.search(x.children[i], k)

	# TODO
	def insert(self, k):
		pass
		# if len(self.root.num_keys)==0:
		# 	self.root.keys.append(k)
		# else:
			

