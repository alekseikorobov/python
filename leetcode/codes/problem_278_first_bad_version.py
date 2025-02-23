#%%
class Solution:
    
    is_bad_version = None
    
    def firstBadVersion(self, n: int) -> int:
        self.curr_bad_index = None
        def isBadVersion(_m):
            #print(f'{self.is_bad_version=}')
            return _m >= self.is_bad_version
        
        def bin_search(min_v, max_v):
            if min_v > max_v:
                return
            l = max_v - min_v
            #print(f'{min_v=}-{max_v=}, {l=}')
            if l == 0:
                b = isBadVersion(max_v)
                if b:
                    self.curr_bad_index = max_v
                return
            if l == 1:
                m = min_v
            else:
                m = (l // 2) + min_v
            b = isBadVersion(m)
            #print(f'{m=},{b=}')
            if b:
                self.curr_bad_index = m
                max_v = m - 1
                #print(f'to left, {max_v=}')
                bin_search(min_v, max_v)
            else:
                min_v = m + 1
                #print(f'to right {min_v=}')
                bin_search(min_v, max_v)
            #print('break')

        self.curr_bad_index = n
        bin_search(1 , n)
        return self.curr_bad_index
    
s = Solution()
s.is_bad_version = 1
res = s.firstBadVersion(3)
print(f'{res=}')

#решил на 1 час 12 минут :(


#%%
class Solution:
    
    is_bad_version = None
    
    def firstBadVersion(self, n: int) -> int:
        def isBadVersion(_m):
            return _m >= self.is_bad_version
        
        start = 1
        end = n
        while(start < end):
            m = ((end - start) // 2) + start
            if isBadVersion(m):
                end = m
            else:
                start = m + 1
        return start
        
        
s = Solution()
s.is_bad_version = 1
res = s.firstBadVersion(3)
print(f'{res=}')