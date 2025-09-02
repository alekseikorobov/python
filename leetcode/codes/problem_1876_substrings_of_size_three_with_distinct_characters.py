class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        k = 3
        N = 0
        l = len(s)
        curr_ss = ''
        for i in range(l):
            if i + k > l:
                break
            for j in range(i, i + k):
                if s[j] not in curr_ss:
                    curr_ss += s[j]
            if len(curr_ss) == k:
                N+=1
            curr_ss = ''
        return N

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        max_k = 3
        l = len(s)
        if l < max_k: return 0
        if l == max_k:
            return 1 if len(set(s)) == l else 0
        N = 0
        for i in range(l-2):
            j = i + 1
            k = i + 2
            
            if s[i] != s[j] and s[i] != s[k] and s[j] != s[k]:
                N+=1
        return N


#%%
def window_fixed_size(nums, k):
    i = 0
    result = None

    for j in range(len(nums)):
        # Expand the window
        # Add nums[j] to the current window logic

        # Ensure window has size of K
        if (j - i + 1) < k:
            continue
        
        print(nums[i:j])
        # Update Result
        # Remove nums[i] from window
        # increment i to maintain fixed window size of length k
        i += 1

    return result

nums = [1,2,3,4,5,6,7,8,9,10]
window_fixed_size(nums,4)


#2025-07-11
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        k = 3
        result_all = []
        for i in range(len(s)):
            result = s[i]
            j = i + 1
            while j < len(s) and s[j] not in result and j-i < k:
                result += s[j]
                j += 1
            if len(result) == k:
                result_all.append(result)
            
        #print(result_all)
        return len(result_all)