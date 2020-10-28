class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s)<=numRows or numRows==1:
            return s
        res = ""
        for i in range(numRows):
            if i==0 or i==numRows-1:
                j=0
                while i+j*2*(numRows-1)<len(s):
                    res = res + s[i+j*2*(numRows-1)]
                    j+=1
            else:
                j=0
                flag = True
                val = i
                while flag:
                    if j%2==0:
                        if val<len(s):
                            res = res+s[val]
                        else:
                            flag = False
                        val = val + 2*(numRows-i-1)
                    else:
                        if val<len(s):
                            res = res+s[val]
                        else:
                            flag = False
                        val = val + 2*(i)
                    j+=1
        return res




l = Solution()
print(l.convert(s = "PAYPALISHIRING", numRows = 3))
print(l.convert(s = "PAYPALISHIRING", numRows = 4))
