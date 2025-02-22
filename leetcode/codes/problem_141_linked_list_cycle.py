# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def stack_loop(self, curr_node):

        if curr_node is None:
            return False

        if hasattr(curr_node,'flg'):
            return True
        
        curr_node.flg = 'has'

        return self.stack_loop(curr_node.next)

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        return self.stack_loop(head)


#O = N