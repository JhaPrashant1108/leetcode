class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x=="":
            return True
        if len(x)==1 and x.isdigit():
            return True
        val = len(x)//2
        for i in range(val):
            if x[i]!=x[len(x)-i-1]:
                return False
        return True





l = Solution()
print(l.isPalindrome(121))
print(l.isPalindrome(-21))
print(l.isPalindrome(10))
print(l.isPalindrome("-"))