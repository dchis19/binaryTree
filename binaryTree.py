class Node:
	def __init__(self, key):
		self.val = key
		self.right = None
		self.left = None

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

def inorder(root):
	if root:
		inorder(root.left)
		print(root.val, end = " ")
		inorder(root.right)

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
