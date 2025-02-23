# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        l = []
        while curr:
            l.append(curr.val)
            curr = curr.next
        demmy = ListNode(val=0)
        curr = demmy
        for i in range(len(l)-1,-1,-1):
            curr.next = ListNode(l[i])
            curr = curr.next

        return demmy.next
        

# посмотрел другое решение:
class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        new_head = None
        curr = head
        while curr:
            temp = curr.next #сохраняем следующий элемент
            curr.next = new_head # меняем положение узла на противоложенный
            new_head = curr #теперь следующий элемент это уже текущий
            curr = temp #переходим к следующему элементу
        return new_head
        
