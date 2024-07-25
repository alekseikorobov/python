from typing import List


class Solution:

    def __init__(self) -> None:
        self.d_p = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z'],
        }

    

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        # if len(digits) == 1:
        #     return self.d_p[digits]

        res = list(self.d_p[digits[0]])
        res1 = list(self.d_p[digits[0]])
        for i in range(1,len(digits)):
            d = digits[i]
            chars = self.d_p[d]
            res1 = []
            for r in res:
                for c in chars:
                    res1.append(r + c)            
            res = list(res1)
        return res1




s = Solution()

def equal_array(arr1:List[str], arr2:List[str]) -> bool:
    if len(arr1) != len(arr2):
        print(f'{len(arr1)=} {len(arr2)=}')
        print(arr1)
        print(arr2)
        return False
    arr1 = set(sorted(arr1))
    
    arr2 = set(sorted(arr2))
    if len(arr1 - arr2) == 0:
        return True
    else:
        print(arr1)
        print(arr2)
        return False

#print(equal_array(s.letterCombinations("23"),["ad","ae","af","bd","be","bf","cd","ce","cf"]))
print(equal_array(s.letterCombinations("234"),["adg","adh","adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"]))
#print(equal_array(s.letterCombinations("2"),["a","b","c"]))
#print(equal_array(s.letterCombinations(""),[]))






