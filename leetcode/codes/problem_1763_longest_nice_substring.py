#%%
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        print(s)
        
        def get_store(s):        
            store = {}
            for c in s:
                c_l = c.lower()
                if c_l not in store:
                    store[c_l] = [0,0]
                index = 1 if c.isupper() else 0
                store[c_l][index] = 1
            return store

        start = 0
        result = ''
        max_res = ''
        a = 0
        #store[s[a].lower()] = [0,1] if s[a].isupper() else [1,0]

        store = get_store(s)
        store_split_char = [c if store[c][0] == 1 else c.upper() for c in store if sum(store[c]) == 1]
        print(f'{store_split_char=}')
        
        split_strs = []
        if len(store_split_char)>0:
            start = 0
            for i in range(len(s)):
                if s[i] in store_split_char:
                    if start<i:
                        split_strs.append(s[start:i])
                    start = i+1
            if start<i:
                split_strs.append(s[start:i+1])
            print(split_strs)
        else:
            split_strs.append(s)
        
        for line in split_strs:
            start = 0
            a = 0
            store = get_store(line)
            print(f'{line=},{store=}')
            while a < len(line):
                start = a
                result = ''
                while start < len(line) and line[start].lower() in store and sum(store[line[start].lower()]) == 2:
                    result += line[start]
                    start+=1
                print(f'{result=}')
                if len(result)>len(max_res):
                    max_res = result
                a += 1
        
        return max_res


s = Solution()
#s.longestNiceSubstring("zzabvogdeABVGoDEZ")
#s.longestNiceSubstring("zzabvogdeABVGDEZo")
#s.longestNiceSubstring("YazaAay")
#s.longestNiceSubstring("Bb")
#s.longestNiceSubstring("YaxaAaaBaba") #aAaaBaba
s.longestNiceSubstring("FeOZJEnNfjz") #nN


#%%
#не смог решить, решение из ответов:
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if not s: return "" # boundary condition 
        ss = set(s)
        for i, c in enumerate(s):
            if c.swapcase() not in ss: 
                s0 = self.longestNiceSubstring(s[:i])
                s1 = self.longestNiceSubstring(s[i+1:])
                return max(s0, s1, key=len)
        return s
            