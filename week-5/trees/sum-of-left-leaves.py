# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def __init__(self):
        self.sum_of_left_leaves = 0
    
    def addLeft(self, node):
        self.sum_of_left_leaves += node.val
        
    def traverseForLeftLeaves(self, root: TreeNode, isLeft: bool):
        if not root:
            return
        # left leaf found
        elif not root.left and not root.right and isLeft:
            self.addLeft(root)
            
        self.traverseForLeftLeaves(root.left, True)
        self.traverseForLeftLeaves(root.right, False)
        
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.traverseForLeftLeaves(root, False)
        return self.sum_of_left_leaves