# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def __init__(self):
        self.ls = []
    
    def clearLeafSeq(self):
        self.ls = []
    
    def getLeafSequence(self, root):
        if not root:
            return
        elif not root.left and not root.right:
            self.ls.append(root.val)
            return
        
        self.getLeafSequence(root.left)
        self.getLeafSequence(root.right)
        
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1:
            return not root2
        elif not root2:
            return not root1 
        
        self.getLeafSequence(root1)
        leaf_seq_1 = tuple(self.ls)
        
        self.clearLeafSeq()
        
        self.getLeafSequence(root2)
        leaf_seq_2 = tuple(self.ls)
        
        return leaf_seq_1 == leaf_seq_2