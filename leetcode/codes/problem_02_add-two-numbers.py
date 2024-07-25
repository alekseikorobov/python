# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    
    def get_num(self, l1: Optional[ListNode]):
        num1 = l1.val
        _next = l1.next
        i = 1
        while not _next is None:
            n_v = _next.val * (10 ** i)
            num1 += n_v
            #print('num1',num1,'n_v',n_v)
            _next = _next.next
            i += 1
        return num1

    def int_to_ListNode(self, num: str, l : ListNode):
        #print('num',num)
        res_str = num
        n = int(res_str[0])
        #print('n',n)
        l.val = n       
        if len(res_str[1:]) > 0:
            l.next = self.int_to_ListNode(res_str[1:],ListNode())            
        return l

    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = self.get_num(l1)
        n2 = self.get_num(l2)
        res = n1 + n2
        return self.int_to_ListNode(res)

        

s = Solution()
#r = s.int_to_ListNode('807',ListNode())

r = ListNode(7)
r.next = ListNode(0)
r.next.next = ListNode(8)

n = s.get_num(r)
print(n)

