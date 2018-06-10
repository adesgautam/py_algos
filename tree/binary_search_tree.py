
# Structure of the BST Node
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

# Insert node in BST O(h)
def insert(root, node):
	if root is None:
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

# Search node having x as value O(h)
def search_x(root, x):
	if root is None:
		return "value not found"
	if root.val == x:
		return "value found"
	elif root.val > x:
		return search_x(root.left, x)
	else:
		return search_x(root.right, x)

# For delete function (find inorder successor)
def minnode(root):
	current = root
	while(current.left is not None):
		current = current.left
	return current

# Delete node having x as value O(h)
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

# For height function
def max(a, b):
	if a>b:
		return a
	else:
		return b

# Find height of BST O(n)
def height(root):
	if root is None:
		return 0
	leftheight = height(root.left)
	rightheight = height(root.right)
	return max(leftheight, rightheight)+1

# For isBST function
def isSmaller(root, x):
	if root is None:
		return True
	if root.val <= x and isSmaller(root.left,x) and isSmaller(root.right,x):
		return True
	else:
		return False

# For isBST function
def isGreater(root, x):
	if root is None:
		return True
	if root.val > x and isGreater(root.left,x) and isGreater(root.right,x):
		return True
	else:
		return False

# Check is binary tree is BST 0(n^2) (Method 1)
def isBST(root):
	if root is None:
		return True
	if isSmaller(root.left, root.val) and isGreater(root.right, root.val) and isBST(root.left) and isBST(root.right):
		return True
	else:
		return False

# For isBST_by_inorder function (Create inorder list of BST O(n) )
inorderL = []
def create_inorder_list(root):
	if root:
		create_inorder_list(root.left)
		inorderL.append(root.val)
		create_inorder_list(root.right)

# For isBST_by_inorder function (Check if list is sorted)
def checkSorted(li):
	for i in range(len(li)-1):
		if not li[i] <li[i+1]:
			return False
	return True

# Check is Binary tree is BST (Method 2)
def isBST_by_inorder(root):
	create_inorder_list(root)
	if checkSorted(inorderL):
		return True
	
# Inorder Traversal O(n)
def inorder(root):
	if root:
		inorder(root.left)
		print(root.val, end=" ")
		inorder(root.right)

# Preorder Traversal O(n)
def preorder(root):
	if root:
		print(root.val, end=" ")
		preorder(root.left)
		preorder(root.right)

# Postorder Traversal O(n)
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

print(isBST(root))

print(isBST_by_inorder(root))




