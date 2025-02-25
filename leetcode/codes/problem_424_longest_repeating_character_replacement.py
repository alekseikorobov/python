#%%
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #store = defaultdict(int)
        store = []
        max_char = ''
        max_count = 0
        curr_char = s[0]
        curr_count = 1
        for i in range(1,len(s)):
            
            if s[i] != curr_char:
                store.append((curr_char,curr_count))
                curr_char = s[i]
                curr_count = 1
            else:
                curr_count+=1

                if curr_count > max_count:
                    max_count = curr_count
                    max_char = curr_char
        
        
        store.append((curr_char,curr_count))
        
        print(f'{store=}')
        
        for item in store:
                
        

        res = max_count + k
        if res>len(s):
            res = len(s)

        return res
    
s = Solution()
s.characterReplacement("AABABBA",1)
#%%
        



        
        
        
        # нерабочее решение
        # max_result = ''
        # for i in range(len(s)):
        #     _k = k
        #     next_i = i+1
        #     result = s[i]
        #     next_char = ''
        #     if next_i < len(s):
        #         next_char = s[next_i]
        #         if next_char != s[i] and _k > 0:
        #             _k -= 1
        #             next_char = s[i]
        #     while s[i] == next_char:
        #         result += next_char
        #         next_i+=1
        #         if next_i >= len(s): break
        #         next_char = s[next_i]
        #         if next_char != s[i] and _k > 0:
        #             _k -= 1
        #             next_char = s[i]
        #     if len(result)> len(max_result):
        #         max_result = result
        
        # return max_result