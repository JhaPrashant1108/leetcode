class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        for digit in num:
            while st and st[-1]>digit and k:
                st.pop()
                k-=1
            st.append(digit)
        while k>0:
            st.pop()
            k-=1
        ans = "".join(st).lstrip("0")
        if ans!="":
            return ans
        else:
            return "0"
















l = Solution()
print(l.removeKdigits("1432219",3))
print(l.removeKdigits("10200",1))
print(l.removeKdigits("10",2))