# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        self.counter = 0

        def loop(node):
            if node is None:
                return
            self.counter+=1
            loop(node.left)
            loop(node.right)
        
        loop(root)
        return self.counter
    
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        
        def loop(node):
            if node is None: return 0
            counter1 = loop(node.left)
            counter2 = loop(node.right)
            return counter1 + counter2 + 1        
        
        return loop(root)