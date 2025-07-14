

#2022-02-06
def lengthOfLongestSubstring(s: str) -> int:
    max_result_str = ''
    res_str = ''
    start_index_char = 0
    i = 0
    while i < len(s):
        c = s[i]
        i += 1
        #print(f'[{i}] = {c}')
        if not c in res_str:
            res_str +=c
            if len(res_str) > len(max_result_str):
                max_result_str = res_str
        else:
            #print('reset')
            res_str = ''
            start_index_char += 1
            i = start_index_char        
    return len(max_result_str)

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring(""))
print(lengthOfLongestSubstring("a"))
print(lengthOfLongestSubstring("aab"))
print(lengthOfLongestSubstring("dvdf")) #must 3

#2024-07-20
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = ''
        max_result = 0
        curr_max = 0
        for i in range(len(s)):
            for index in range(i,len(s)):
                if s[index] not in result:
                    result += s[index]
                    curr_max += 1
                else:
                    if curr_max > max_result:
                        max_result = curr_max
                    result = ''
                    curr_max = 0
                    break
        if curr_max > max_result:
            max_result = curr_max
        return max_result

##2025-02-22
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:        
        max_str = ''
        N = len(s)
        curr_str = ''
        for i in range(0,len(s)):
            curr_str = s[i]
            i1 = i + 1
            while i1 < N and s[i1] not in curr_str:
                curr_str += s[i1]
                i1 += 1
            if len(curr_str) > len(max_str):
                max_str = curr_str

        return len(max_str)
    
##2025-07-11
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_length = 0
        N = len(s)
        for i in range(N):
            result = s[i]
            j = i + 1
            while j < N and s[j] not in result:
                result += s[j]
                j+=1
            if len(result) > max_length:
                max_length = len(result) 
        return max_length