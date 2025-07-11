class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        curr = head
        line_list = []
        while curr:
            line_list.append(curr.val)
            curr = curr.next

        a = 0
        b = len(line_list)-1
        while a <= b:
            if line_list[a] != line_list[b]:
                return False
            a += 1
            b -= 1

        return True
    
#O(N + N/2) = O(2N)
