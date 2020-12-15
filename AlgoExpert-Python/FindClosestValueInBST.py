def findClosestValueInBst(bstNode, target):
	
	# case node is target
	if bstNode.value == target:
		return bstNode.value
	# case node is greater than target and left branch is not empty
	if bstNode.value > target and bstNode.left != None:
		leftVal = findClosestValueInBst(bstNode.left,target)
		if abs(leftVal-target) <= abs(bstNode.value-target):
			return leftVal
		else:
			return bstNode.value
	# case node is less than target and right branch is not empty
	if bstNode.value < target and bstNode.right != None:
		rightVal = findClosestValueInBst(bstNode.right,target)
		if abs(rightVal-target) <= abs(bstNode.value-target):
			return rightVal
		else:
			return bstNode.value
	# case node is greater than target and left branch is empty
	if bstNode.value > target and bstNode.left == None:
		return bstNode.value
	# case node is less than target and right branch is empty
	if bstNode.value < target and bstNode.right == None:
		return bstNode.value


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
