
# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def build_nodes(self, list:List) -> ListNode:        
        node = ListNode(list[0], None)
        last = node
        for i in range(1,len(list)):
            l = list[i] 
            last.next = ListNode(l, None)
            last = last.next
        return node
    
    def toArray(self,ns:ListNode):
        el = ns
        res = []
        while el is not None:
            res.append(el.val)
            el = el.next
        return res

    def recurs(self,preview: Optional[ListNode],node: Optional[ListNode]) -> Optional[ListNode]:
        last_node = preview
        if node.next is not None:
            last_node = self.recurs(node, node.next)
        
        last_node.next = node
        return last_node
        


    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if isinstance(head, List):
            head = self.build_nodes(head)
        
        cur = self.recurs(head)
        # preview = head
        # i = 1
        # while cur is not None: #1
        #     cur_next = cur.next 
        #     if i == 2:# == 0:
        #         #print('i % 2')
        #         preview.next = cur_next
        #         head = preview
        #     preview = cur #1
        #     cur = cur_next
        #     i += 1


        return cur



s = Solution()


print(s.toArray(s.swapPairs([1,2,3,4])))