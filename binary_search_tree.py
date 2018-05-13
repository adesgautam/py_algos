
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def insert(root, node):
	if root == None:
		root = node

	if root.val < node.val:
		if root.right == None:
			root.right = node
		else:
			insert(root.right, node)
	else:
		if root.left == None:
			root.left = node
		else:
			insert(root.left, node)

def search_x(root, x):
	
	if not root:
		return "value not found"
	if root.val == x:
		return "value found"
	elif root.val > x:
		return search_x(root.left, x)
	else:
		return search_x(root.right, x)

def delete(root, x):
	pass

def inorder(root):
	if root:
		inorder(root.left)
		print(root.val, end=" ")
		inorder(root.right)

def preorder(root):
	if root:
		print(root.val, end=" ")
		preorder(root.left)
		preorder(root.right)

def postorder(root):
	if root:
		print(root.val, end=" ")
		postorder(root.left)
		postorder(root.right)

root = Node(10)
insert(root, Node(40))
insert(root, Node(20))
insert(root, Node(60))
insert(root, Node(30))
insert(root, Node(70))
insert(root, Node(80))
insert(root, Node(90))

# inorder(root)
inorder(root)
f = search_x(root,100)
print(f)








