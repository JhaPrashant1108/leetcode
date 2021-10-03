class Solution:
    def canJump(self, nums):
        maxIndex = 0
        for i, val in enumerate(nums):
            if i > maxIndex:
                return False
            maxIndex = max(maxIndex, i+val)
        return True


L = Solution()
print(L.canJump([2, 3, 1, 1, 4]))
print(L.canJump([3, 2, 1, 0, 4]))
