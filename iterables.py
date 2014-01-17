def simple_iterator():
	return iter([1,2,3])

def simple_generator():
	yield 1
	yield 2
	yield 3

def fibonacci_iterator(max):
	fibs = []
	a,b = 1,1
	while a < max:
		fibs.append(a)
		a,b = b,a+b
	return fibs

def fibonacci_generator(max):
	a,b = 1,1
	while a < max:
		yield a
		a, b = b, a+b

def tree_iterator(tree):
	nodes = []
	if tree.left is not None:
		for node in tree_iterator(tree.left):
			nodes.append(node)
	nodes.append(tree)
	if tree.right is not None:
		for node in tree_iterator(tree.right):
			nodes.append(node)
	return nodes

def tree_generator(tree):
	if tree.left is not None:
		for node in tree_generator(tree.left):
			yield node
	yield tree
	if tree.right is not None:
		for node in tree_generator(tree.right):
			yield node

class TreeNode:
	def __init__(self,value,left=None,right=None):
		self.value = value
		self.left = left
		self.right = right
	
	def __str__(self):
		if self.left == None:
			leftString = '[]'
		else:
			leftString = str(self.left)
		if self.right == None:
			rightString = '[]'
		else:
			rightString = str(self.right)
		return '[' + str(self.value) + ', ' + leftString + ', ' + rightString + ']'

binary_tree = TreeNode(10,TreeNode(7,TreeNode(3,TreeNode(1),TreeNode(5)),TreeNode(8)),TreeNode(12,TreeNode(11),TreeNode(13)))
