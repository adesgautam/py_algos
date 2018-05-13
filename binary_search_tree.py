
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

def minnode(root):
	current = root
	while(current.left is not None):
		current = current.left
	return current

def delete(root, x):
	if root is None:
		return root
	if root.val>x :
		root.left = delete(root.left, x)
	elif root.val<x :
		root.right = delete(root.right, x)
	else:
		if root.left==None:     # 1 child
			temp = root.right
			root = None
			return temp
		elif root.right==None:  # 1 child
			temp = root.left
			root = None
			return temp
		
		# 2 children
		temp = minnode(root.right)
		root.key = temp.key
		root.right = delete(root.right, temp.key)

	return root

def max(a, b):
	if a>b:
		return a
	else:
		return b

def height(root):
	if root is None:
		return 0
	leftheight = height(root.left)
	rightheight = height(root.right)
	return max(leftheight, rightheight)+1

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

inorder(root)
f = search_x(root,40)
print('\n',f)

f = delete(root, 20)
print(f.val)
inorder(root)

# here single node with left and right null, has height=1
print("\n",height(root))








