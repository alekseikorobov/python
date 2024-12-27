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
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if isinstance(list1,List): list1 = self.build_nodes(list1)
        if isinstance(list2,List): list2 = self.build_nodes(list2)

        if list1 is None: return list2
        if list2 is None: return list1

        el1 = list1
        el2 = list2
        
        node = None
        last = None
        #res = []
        while el1 is not None or el2 is not None:
            if el2 is not None and el1 is not None:
                if el2.val <= el1.val:
                    #res.append(el2.val)
                    if node is None:
                        node = ListNode(el2.val, None)
                        last = node
                    else:
                        last.next = ListNode(el2.val, None)
                        last = last.next
                    el2 = el2.next            
                else:
            #res.append(el1.val)
                    if node is None:
                        node = ListNode(el1.val, None)
                        last = node
                    else:
                        last.next = ListNode(el1.val, None)
                        last = last.next
                    el1 = el1.next
            elif el2 is not None:
                if node is None:
                    node = ListNode(el2.val, None)
                    last = node
                else:
                    last.next = ListNode(el2.val, None)
                    last = last.next
                    el2 = el2.next
            else: #el1 is not None:
                if node is None:
                    node = ListNode(el1.val, None)
                    last = node
                else:
                    last.next = ListNode(el1.val, None)
                    last = last.next
                el1 = el1.next
        return node

s = Solution()


print(s.toArray(s.mergeTwoLists([1,2,4],[1,3,4])))
print(s.toArray(s.mergeTwoLists([1],[2])))
