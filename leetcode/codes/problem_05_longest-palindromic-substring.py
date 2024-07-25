

from typing import List


class Solution:
    def show(self,s,index_left,index_right):
        print(f's_l[{index_left}] = {s[index_left]}, s_r[{index_right}] = {s[index_right]}')


    def longestPalindrome(self, s: str) -> str:
        index_left = 0
        index_right = len(s)-1
        start_index_left = 0
        a,b = index_left,index_right
        start = False
        for index_right_i in range(index_right,-1,-1):
            
            self.show(s,index_left,index_right_i)

            if index_right_i == index_left:
                print('break')
                break

            if s[index_right_i] == s[index_left]:
                print('index_left + 1')
                index_left += 1
                start = True
            elif start:
                index_left = start_index_left
                index_right -= 1
                start = False
            else:
                index_right -= 1
            
            


        # while s[index_left] == s[index_right]:
        #     index_left += 1
        #     index_right -= 1
        #     if index_left == index_right:
        #         break

        return ''#s[a:b+1]



s = Solution()

print('12321->123211', s.longestPalindrome('123211') )
#print('babad->bab', s.longestPalindrome('babad') )