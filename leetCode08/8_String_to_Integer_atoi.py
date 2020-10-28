class Solution:
    def myAtoi(self, s: str) -> int:
        flag = True
        # s = s.replace(" ","")
        s = s.lstrip()
        if s=="":
            return 0
        s = s.split()[0]
        res = ""
        if s[0]=="-":
            flag = False
            s = s[1:]
        elif s[0]=="+":
            s = s[1:]

        for i in range(len(s)):
            if s[i].isdigit():
                res = res + s[i]
            else:
                break
        if res == "":
            return 0
        if int(res)>2147483647 and flag==True:
            return 2147483647
        if int(res)>2147483648 and flag == False:
            return -2147483648
        if flag == False:
            return -1*int(res)
        return int(res)






l = Solution()
print(l.myAtoi("42"))
print(l.myAtoi("   -42"))
print(l.myAtoi("4193 with words"))
print(l.myAtoi("words and 987"))
print(l.myAtoi("-91283472332"))