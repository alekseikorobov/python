

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_nodes(list:List) -> ListNode:
    if len(list) == 0:
        return None
    node = ListNode(list[0], None)
    last = node
    for i in range(1,len(list)):
        l = list[i]
        last.next = ListNode(l, None)
        last = last.next
    return node
    
def toArray(ns:ListNode):
    el = ns
    res = []
    while el is not None:
        res.append(el.val)
        el = el.next
    return res