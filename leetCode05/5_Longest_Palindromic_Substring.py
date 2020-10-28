class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindromeChecker(s,left,right,length):
            if s=="" or left<0 or right>=len(s):
                return length
            if s[left]==s[right]:
                length = s[left]+length+s[right]
                left = left-1
                right = right+1
                length = palindromeChecker(s,left,right,length)

            return length

        resE = ""
        resO = ""
        for i in range(len(s)):
            valE = palindromeChecker(s,i,i+1,"")
            if len(valE)>= len(resE):
                resE=valE
            valO = palindromeChecker(s,i-1,i+1,s[i])
            if len(valO)>= len(resO):
                resO = valO
        if len(resE)>len(resO):
            return resE
        else:
            return resO




l = Solution()
print(l.longestPalindrome("babad"))
print(l.longestPalindrome("cbbd"))
print(l.longestPalindrome("sdababaz"))
print(l.longestPalindrome("aaaa"))