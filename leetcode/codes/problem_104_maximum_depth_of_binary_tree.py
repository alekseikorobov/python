# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs_preorder(self,node, deep = 0):
        if node is None:
            return deep
        deep_left = self.dfs_preorder(node.left, deep+1)
        deep_right = self.dfs_preorder(node.right, deep+1)
        
        return max(deep_left,deep_right)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs_preorder(root)


        