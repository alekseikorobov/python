# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#variant 1
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = l1
        b = l2
        result_list = []
        v_l = 0
        while a is not None or b is not None:
            v1 = 0
            v2 = 0
            if a is not None:
                v1 = a.val
                a = a.next
            if b is not None:
                v2 = b.val
                b = b.next
            v = v1 + v2 + v_l
            if v > 9:
                v_l, v = v//10 , v%10
            else:
                v_l = 0
            
            result_list.append(v)
            
        if v_l>0:
            result_list.append(v_l)
        
        result = ListNode(result_list[0])
        curr = result
        for i in range(1,len(result_list)):
          curr.next = ListNode(val=result_list[i])
          curr = curr.next
        return result

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = l1
        b = l2
        result = None
        curr = None
        v_l = 0
        while a is not None or b is not None:
            v1 = 0
            v2 = 0
            if a is not None:
                v1 = a.val
                a = a.next
            if b is not None:
                v2 = b.val
                b = b.next
            v = v1 + v2 + v_l
            if v > 9:
                v_l, v = v//10 , v%10
            else:
                v_l = 0
            
            if result is None: #is first
                result = ListNode(v)
                curr = result
            else:
                curr.next = ListNode(v)
                curr = curr.next 
            
        if v_l>0:
            curr.next = ListNode(v_l)
        
        return result