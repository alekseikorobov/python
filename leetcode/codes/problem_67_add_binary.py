class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        #if len(a)<len(b) return addBinary
        
        i = len(a) - 1
        j = len(b) - 1
        result = []
        buff = '0'
        while i >= 0 or j >= 0:
            a_i = a[i] if i >= 0 else '0'
            b_i = b[j] if j >= 0 else '0'

            
            if buff == '1' and (a_i == '1' and b_i == '1'):
                result.append(buff)
            elif buff == '1' and (a_i == '1' or b_i == '1'):
                result.append('0')
            elif buff == '1' and (a_i == '0' and b_i == '0'):
                buff = '0'
                result.append('1')
            elif buff == '0' and (a_i == '1' and b_i == '1'):
                buff = '1'
                result.append('0')
            elif buff == '0' and (a_i == '1' or b_i == '1'):
                result.append('1')
            elif buff == '0' and (a_i == '0' and b_i == '0'):
                result.append('0')

            i-=1
            j-=1
        if buff == '1':
            result.append('1')

        result.reverse()
        return ''.join(result)


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        #if len(a)<len(b) return addBinary
        
        i = len(a) - 1
        j = len(b) - 1
        result = []
        buff = 0
        while i >= 0 or j >= 0:
            a_i = int(a[i]) if i >= 0 else 0
            b_i = int(b[j]) if j >= 0 else 0

            n = a_i + b_i + buff
            #print(n)
            if n == 3:
                buff = 1
                result.append(1)
            elif n == 2:
                buff = 1
                result.append(0)
            else:
                buff = 0
                result.append(n)

            i-=1
            j-=1
        if buff>0:
            result.append(buff)

        result.reverse()
        return ''.join(map(str,result))
#O(N+M)