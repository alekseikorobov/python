class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        N = len(s)
        left = 0
        right = N - 1

        while left < right:

            c_left = s[left]
            c_right = s[right]
            print(c_left.isdigit(),c_left.isalpha())
            while (not c_left.isdigit() and not c_left.isalpha()):
                print(f'skip {c_left=}')
                if left + 1 < N:
                    left += 1
                    c_left = s[left]
                else:
                    c_left = ""
                    break

            while (not c_right.isdigit() and not c_right.isalpha()):
                print(f'skip {c_right=}')
                if right > 0:
                    right -= 1
                    c_right = s[right]
                else:
                    c_right = ""
                    break

            c_left = c_left.lower()
            c_right = c_right.lower()
            
            print(f'{c_left=} {c_right=}')

            if c_left != c_right:
                return False

            left += 1
            right -= 1

        return True

s = Solution()
result = s.isPalindrome(".,")
print(result)

#O(N)