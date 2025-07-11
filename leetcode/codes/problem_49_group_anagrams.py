#%%
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        def get_hash(a):
            t = {k:0 for k in 'qwertyuiopasdfghjklzxcvbnm'}
            for c in a:
                t[c]+=1
            return ','.join([str(t[k]) for k in t])
            #return tuple(t.values()) # так работает медленнее

        d = {}
        for a in strs:
            a_s = get_hash(a)
            #a_s = ''.join(sorted(a)) # так тоже можно, но работает медленнее
            #print(a,a_s)
            if a_s in d:
                d[a_s].append(a)
            else:
                d[a_s] = [a]
        
        return list(d.values())
    
strs = ["aaaaaaaaaaabcdefghijklmnopqrstuvwxyz","abbbbbbbbbbbcdefghijklmnopqurstuvwxyz","abcccccccccccdefghijklmnopqurstuvwxyz"]
s = Solution()
s.groupAnagrams(strs)