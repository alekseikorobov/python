class Solution:
    def countAndSay(self, n: int) -> str:        
        
        if n == 1:
            return '1'
        
        s = self.countAndSay( n - 1 )

        curr = s[0]
        count = 1

        res = ''
        for i in range(1,len(s)):
            c = s[i]
            if c == curr:
                count += 1
            else:
                res += str(count) + curr
                curr = c
                count = 1
        
        res += str(count) + curr
        return res




s = Solution()


#print(f'{s.countAndSay(1) == "1" = }')

# print(f'{s.countAndSay(2) == "11" = }')
# print(f'{s.countAndSay(3)=}, 21')
# print(f'{s.countAndSay(4)=}, 1211')
print(f'{s.countAndSay(5)=}, 111221')
print(f'{s.countAndSay(6)=}, 312211')