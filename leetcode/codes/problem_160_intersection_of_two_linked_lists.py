# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        # рабочее решение но не уместились по времени
        # fast = headA
        # slow = headB

        # while slow:
        #     while fast:
        #         if slow == fast:
        #             return fast
        #         fast = fast.next
        #     slow = slow.next
        #     fast = headA
        
        
        fast = headA
        slow = headB
        while fast:
            fast.has = 1
            fast = fast.next
        while slow:
            if hasattr(slow,'has'):
                return slow
            slow = slow.next        
        # O(N+M)
        
        
        # чужое решение:
        # lista = headA
        # listb = headB

        # while lista != listb:
        #     lista = lista.next if lista else headB
        #     listb = listb.next if listb else headA
        
        # return listb
        
        return None

            