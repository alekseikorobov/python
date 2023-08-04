class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == "0" or num2 == "0": 
            return "0"

        res = []

        num1 = num1[::-1]
        num2 = num2[::-1]
        it = 0
        ld = 0
        for n2 in num2:
            ld = 0
            p = 0
            for n1 in num1:
                n2_i = int(n2)
                n1_i = int(n1)
                
                r = (n2_i * n1_i) + ld
                r,ld = r % 10, r // 10

                if it > 0 and it + p < len(res):
                    n = int(res[it + p])
                    n += r
                    if n > 9:
                        ld += n // 10
                        n = n % 10
                    res[it + p] = str(n)
                else:
                    res.append(str(r))
                p += 1

            if ld > 0:
                res.append(str(ld))
            it += 1

        
        return ''.join(res[::-1])


s = Solution()

# print(f'{s.multiply("14","2") = }')

# print(f'{s.multiply("19","2") = }')
# print(f'{s.multiply("100","2") = }')
# print(f'{s.multiply("10","12") = }')
# print(f'{s.multiply("2","12") = }')

# print(f'{s.multiply("200","12") = }')
# print(f'{s.multiply("200","120") = }')

# print(f'{s.multiply("9","9") = }')

#print(f'{s.multiply("99","9") = }') 891 

# print(f'{s.multiply("9","99") = }')

print(f'{s.multiply("9133","0") = }')

#print(f'{s.multiply("408","5") = }')