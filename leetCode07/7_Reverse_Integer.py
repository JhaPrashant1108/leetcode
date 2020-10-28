class Solution:
    def reverse(self, x: int) -> int:
        flag = True
        if x < 0:
            x = -1*x
            flag = False
        x = list(str(x))
        x.reverse()
        x = "".join(x)
        x = int(x)
        if x>2147483647 or x<-2147483648:
            return 0
        if flag:
            return x
        else:
            return -1*x


        


l = Solution()

print(l.reverse(123))
print(l.reverse(-123))
print(l.reverse(120))