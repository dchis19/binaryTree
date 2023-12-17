"""
Node class is used to store instances of each binaryTree
"""

class Node:
	def __init__(self, key):
		self.val = key
		self.right = None
		self.left = None

"""
Insert(root, key) adds the key value into the binary tree. If root is None (ie top of tree), then we make the binary tree. If the
value is less than the key, we add the value to the right side of the node. If the root is larger than the key, we add the value to 
the left side of the node.
"""

def insert(root, key):
	if root is None:
		return Node(key)
	else: 
		if root.val == key:
			return root
		elif root.val>key:
			root.left = insert(root.left, key)
		else:
			root.right = insert(root.right, key)
	return root

"""
inorder(root) iterates through the binary tree and prints the values in the order from smallest to largest
"""

def inorder(root):
	if root:
		inorder(root.left)
		print(root.val, end = " ")
		inorder(root.right)

"""
search(root, key) performs a search of the tree based on a key value. If the key value is found in the tree, the root is returned.
Otherwise None is returned as the entire tree is iterated through. 
"""

def search(root, key):
	if root is None or root.val == key:
		return root
	if root.val < key:
		return search(root.right, key)
	return search(root.left, key)

if __name__ == '__main__':
	r = Node(50)
	r = insert(r, 30)
	r = insert(r, 130)
	r = insert(r, 505)
	inorder(r)

	key = 350
	if search(r, key) is None:
		print(key, "NOT FOUND")
	else: 
		print(key, "FOUND")
