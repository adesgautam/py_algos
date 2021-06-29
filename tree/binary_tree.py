
# Structure of the BST Node
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

# Insert node in BST O(h)
def insert(root, node):


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
		root = node
	t, s = root
	while t.next != None:
		t = t.next
	while s.next != None:

		

# Find height of BST O(n)
def height(root):
	if root is None:
		return 0
	else:
		return max(height(root.left), height(root.right))+1

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
insert(root, Node(20))
insert(root, Node(50))
insert(root, Node(35))
insert(root, Node(44))
insert(root, Node(9))
insert(root, Node(15))
insert(root, Node(62))
insert(root, Node(11))
insert(root, Node(13))

inorder(root)
f = search_x(root,9)
print('\n',f)

f = delete(root, 20)
print(f.val)
inorder(root)

# here single node with left and right null, has height=1
print("\n",height(root))

print(isBST(root))

print(isBST_by_inorder(root))




