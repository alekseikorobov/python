

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
