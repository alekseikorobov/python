from typing import List
class Solution:
    def __init__(self,is_test=False):
        if is_test:
          self.print = print
          self.print('test mode')
        else:
          self.print = lambda *x:None

    def bin_search_min(self, a,l=0,r=0, deep = 0):
        if deep>100:
            raise(Exception('deep 101'))
        if deep == 0:
            l, r = 0,len(a)-1
        # print(f'{l=}, {r=}, {a[l:r+1]=}, {deep=}')
        max_count = 100
        curr_count = 0
        while l <= r:
            if curr_count>max_count:
                raise(Exception('curr more max'))
            curr_count+=1
            m = ((r - l) // 2) + l
            if m + 1 >= len(a):
                return False,0
            m_next = m + 1
            # print(f'{m=}, {a[m]=}, {m_next=}')
            if a[m] < a[m_next]:
                is_find,val = self.bin_search_min(a, m + 1,r,deep+1)
                if is_find:
                    return is_find,val
                else:
                    return self.bin_search_min(a,l,m - 1,deep+1)
            # elif a[m] < t:
            #   l = m + 1
            #   return bin_search(a[l:r+1],t,deep+1)
            else:
                return True,m_next
        return False,0

    def bin_search(self, a, t, l=0, r=0, deep = 0):
  
        if deep == 0:
            l, r = 0,len(a)-1
        #print(f'{l=}, {r=}, {a[l:r+1]=}, {deep=}')
        while l <= r:
            m = ((r - l) // 2) + l
            #print(f'{m=}, {a[m]=}, {t=}')
            if a[m] > t:
                r = m - 1
                return self.bin_search(a,t, l, r,deep+1)
            elif a[m] < t:
                l = m + 1
                return self.bin_search(a,t, l, r,deep+1)
            else:
                return True, m
        return False, -1

    def search(self, nums: List[int], target: int) -> int:
        a = nums
        _,k = self.bin_search_min(a)
        N = len(a)
        a_new = [*a[k:N],*a[0:k]]
        self.print(a_new)
        #target = 4
        is_find, index = self.bin_search(a_new,target)
        self.print(k, index,len(a), index + k)
        if is_find:
          res = index + k
          if res >= len(a):
              res -= len(a)
          return res
        return -1