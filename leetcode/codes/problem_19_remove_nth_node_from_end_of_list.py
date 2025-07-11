from typing import List, Optional


# Definition for singly-linked list.
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


    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:        
        if isinstance(head,List):
            ns = self.build_nodes(head)
        else:
            ns = head

        el = ns
        preview_element = None
        count = 1
        while el.next is not None:
            el = el.next
            count += 1

        count_target = count - n #5 - 2 = 3
        
        el = ns
        while el is not None:
            if count_target == 0:
                if preview_element is not None:
                    preview_element.next = el.next
                    break
                else:
                    ns = el.next
                    break
            preview_element = el
            el = el.next
            count_target -= 1 # 2 1 0
        
        return ns

s = Solution()

print(s.toArray(s.removeNthFromEnd([1,2,3,4,5],2)))
print(s.toArray(s.removeNthFromEnd([1,2,3,4,5],1)))
print(s.toArray(s.removeNthFromEnd([1,2],1)))
print(s.toArray(s.removeNthFromEnd([1],1)))
print(s.toArray(s.removeNthFromEnd([1,2,3,4,5],5)))