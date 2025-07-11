from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        state = 0
        _store = defaultdict(int)
        for c1 in s1:
            _store[c1]+=1
        
        store = _store.copy()
        start_i = 0
        i = 0
        while i < len(s2):
            c2 = s2[i]

            if c2 in store:
                if state == 0: 
                    state = 1
                    start_i = i
                store[c2] -= 1
                if store[c2] == 0:
                    del store[c2]
                if len(store) == 0:
                    return True
            else:
                if state == 1:
                    i = start_i
                    store = _store.copy()
                state = 0
            i += 1
        return False

#O(N)
            
