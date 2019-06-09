# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def __init__(self):
        self.is_same_tree = True
    
    def doubleTraverse(self, root1, root2):
        if not root1 and not root2:
            return
        elif not root1 or not root2:
            self.is_same_tree = False
            
        elif root1.val == root2.val:
            self.doubleTraverse(root1.left, root2.left)
            self.doubleTraverse(root1.right, root2.right)

        else:
            self.is_same_tree = False
            
        
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        self.doubleTraverse(p, q)
                
        return self.is_same_tree