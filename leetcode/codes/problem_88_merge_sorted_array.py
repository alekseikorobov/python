class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        a,b = m-1,n-1
        i = m + n-1
        while a >= 0 or b >= 0:
            v1 = nums1[a] if a >= 0 else float('-inf')
            v2 = nums2[b] if b >= 0 else float('-inf')
            if v1 > v2:
                nums1[i] = v1
                a-=1
            else:
                nums1[i] = v2
                b-=1
            i-=1
# O(N+M)

# после просмотра ответа            
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        a,b = m-1,n-1
        i = m + n-1
        while b >= 0:
            if a>=0 and nums1[a] > nums2[b]:
                nums1[i] = nums1[a]
                a-=1
            else:
                nums1[i] = nums2[b]
                b-=1
            i-=1
# второй способ
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2
        nums1.sort()