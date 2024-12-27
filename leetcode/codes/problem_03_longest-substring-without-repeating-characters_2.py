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
