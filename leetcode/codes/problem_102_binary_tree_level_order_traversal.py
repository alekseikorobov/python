# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#это не рабочий результат, но можно доделать, если добавить глубину. Как в следующем варианте
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:       
        
        result = []
        def bfs(node):
            if node is None:
                return node.val
            curr_arr = []
            if node.left:
                curr_arr.append(node.left.val)
            if node.right:
                curr_arr.append(node.right.val)

            if len(curr_arr)>0:
                result.append(curr_arr)
            if node.left:
                bfs(node.left)
            if node.right:
                bfs(node.right)

        demmy = TreeNode(None,left=root)
        bfs(demmy)

        return result


# рабочий вариант!
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:       
        
        def bfs(root):
            if root is None: return []
            deep = 0
            queue = deque([(root,deep)])
            result = {}
            while queue:
                node,deep = queue.popleft()
                if node:
                    #print(node.val,i)
                    if deep in result:
                        result[deep].append(node.val)
                    else:
                        result[deep] = [node.val]
                    queue.append((node.left,deep+1))
                    queue.append((node.right,deep+1))
                    
            return list(result.values())
        
        return bfs(root)