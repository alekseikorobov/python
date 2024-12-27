class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        Na = len(s)

        Nb = len(p)


        a = 0
        b = 0

        while a > Na: # and b > Nb:
            ac = s[a]
            while b > Nb:
                bc = p[b]
                if ac == bc or p[i] == '?':
                    b += 1
                elif bc == '*':
                    a += 1
                else:
                    return False
        
        # for c in s:
        #     i = 0
        #     if i == N:
        #         return False
        #     while i < N:
        #         if p[i] == c or p[i] == '?':
        #             i += 1
        #             break
        #         elif p[i] == '*':
        #             break
        #         elif p[i] != c:
        #             return False
                    
        return True



s = Solution()

print(f'{s.isMatch("aa", "a") == False = }')
print(f'{s.isMatch("aa", "aa") == True = }')
print(f'{s.isMatch("aab", "aab") == True = }')
print(f'{s.isMatch("aab", "ab") == False = }')

print(f'{s.isMatch("aa", "?") == False = }')
print(f'{s.isMatch("aa", "?a") == True = }')
print(f'{s.isMatch("aab", "?ab") == True = }')
print(f'{s.isMatch("aab", "?b") == False = }')

print(f'{s.isMatch("aa", "a?") == True = }')
print(f'{s.isMatch("aab", "a?ab") == False = }')

print(f'{s.isMatch("aa", "a?a") == False = }')
print(f'{s.isMatch("aab", "a?b") == True = }')



print(f'{s.isMatch(s = "aa", p = "*") == True = }')
print(f'{s.isMatch(s = "cb", p = "?a") == False = }')