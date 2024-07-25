

from typing import List


class Solution:
    def show(self,arr):
        for l in arr:
            print(l)
    def generate_arra(self, s: str, numRows: int):
        arr = []
        row_now = 0
        row_z = 0
        iterat = 0
        isstart = True
        for i in range(0,len(s)):            
            if iterat < numRows:
                if isstart:
                    arr.append('')    
                    isstart = False
                arr[row_now] += s[i]
            else:
                if ((numRows-1) - (row_z + 1)) > 0:
                    row_now +=1
                    row_z += 1
                    arr.append((' '*((numRows-1) - row_z)) +  s[i])
                else:
                    iterat = 0
                    #isstart = True
                    row_now += 1
                    row_z = 0
                    arr.append(s[i])
            
            iterat += 1
        
        return arr

    def convert(self, s: str, numRows: int) -> str:
        arr = self.generate_arra(s,numRows)
        #self.show(arr)

        reslut = ''
        for line_index in range(0,numRows):
            for str in arr:
                if line_index < len(str) and str[line_index] != ' ':
                    reslut += str[line_index]

        return reslut



s = Solution()

# print('1234567890 -> PAHNAPLSIIGYIR  = ',s.convert('1234567890',3))
# print()
# print('1234567890 -> PAHNAPLSIIGYIR  = ',s.convert('1234567890',4))
# print()
# print('1234567890 -> PAHNAPLSIIGYIR  = ',s.convert('12345678901234567890',5))

res = s.convert('PAYPALISHIRING',3)
print('PAYPALISHIRING 3 -> PAHNAPLSIIGYIR  = ',res,res== 'PAHNAPLSIIGYIR')

res = s.convert('PAYPALISHIRING',4)
print('PAYPALISHIRING 4 -> PINALSIGYAHRPI  = ',res,res== 'PINALSIGYAHRPI')


res = s.convert('A',4)
print('A 4 -> A  = ',res,res== 'A')