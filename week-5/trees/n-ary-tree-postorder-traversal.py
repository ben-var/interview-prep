"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def __init__(self):
        self.traversal = []
    
    def traverse(self, root: 'Node'):
        if not root.children:
            self.traversal.append(root.val)
            return
                
        for child in root.children:
            self.postorder(child)
        
        self.traversal.append(root.val)
        
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        self.traverse(root)
        return self.traversal