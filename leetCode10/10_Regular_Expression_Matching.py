class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p)==0:
            return len(s)==0
        firstMatch = len(s)>0 and (s[0]==p[0] or p[0]==".")
        if len(p)>=2 and p[1]=="*":
            return self.isMatch(s,p[2:]) or (firstMatch and self.isMatch(s[1:],p))
        else:
            return firstMatch and self.isMatch(s[1:],p[1:])
        





l = Solution()
print(l.isMatch(s = "aa",p = "a"))
print(l.isMatch(s = "aa",p = "a*"))
print(l.isMatch(s = "ab",p = ".*"))
print(l.isMatch(s = "aab",p = "c*a*b"))
print(l.isMatch(s = "mississippi",p = "mis*is*p*."))
