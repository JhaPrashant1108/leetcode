class Solution:
    def nCr(self, n, r):
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        if r > n:
            return 0
        if r > n-r:
            r = n-r
        mod = 10**9 + 7
        arr = list(range(n-r+1, n+1))
        ans = 1
        for i in range(1, r+1):
            j = 0
            while j < len(arr):
                x = gcd(i, arr[j])
                if x > 1:
                    arr[j] //= x
                    i //= x
                if arr[j] == 1:
                    del arr[j]
                    j -= 1
                if i == 1:
                    break
                j += 1
        for i in arr:
            ans = (ans*i) % mod
        return ans

    def climbStairs(self, n: int) -> int:
        num = n//2
        val = 0
        for i in range(num+1):
            val = val + self.nCr(n-i, i)
        return val


L = Solution()
print(L.climbStairs(2))
print(L.climbStairs(3))
