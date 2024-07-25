from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = []
        dect = {}
        for i in range(0,len(temperatures)):
            now_temp = temperatures[i]            
            is_found = False
            if i + 1 < len(temperatures):
                for i1 in range(i+1,len(temperatures)):
                    nex_temp = temperatures[i1]
                    #print(f'{now_temp=} {nex_temp=}')
                    if nex_temp > now_temp:
                        is_found = True
                        dect[nex_temp] = (i1,i)

                        res.append(i1-i)
                        break
            if not is_found:
                res.append(0)

        return res




s = Solution()


# print(s.dailyTemperatures([73,74,75,71,69,72,76,73])) #[1,1,4,2,1,1,0,0]

# print(s.dailyTemperatures([30,40,50,60])) #[1,1,1,0]
# print(s.dailyTemperatures([30,60,90])) #[1,1,0]
# print(s.dailyTemperatures([30,30,90])) #[2,1,0]

print(s.dailyTemperatures([1,1,1,1]))