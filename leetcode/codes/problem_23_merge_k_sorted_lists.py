

from typing import List,Optional
import codes.common as common

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #создаем произвольное число указателей
        curs = [n for n in lists if n is not None]        
        dymmyNode = ListNode()
        curr = dymmyNode
        
        while len(curs) > 0:
            vals = [n.val for n in curs]
            min_index = 0
            for i in range(1, len(vals)):
                if vals[i] < vals[min_index]:
                    min_index = i
            
            curr.next = ListNode(vals[min_index])
            curr = curr.next
            curs[min_index] = curs[min_index].next
            
            curs = [n for n in curs if n is not None]
                
        return dymmyNode.next