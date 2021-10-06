class Solution(object):
    def findDuplicates(self, nums):
        duplicate = []
        for i in range(len(nums)):
            num = abs(nums[i])
            if nums[num - 1] < 0:
                duplicate.append(num)
                continue
            nums[num - 1] = -nums[num - 1]
        return duplicate


L = Solution()
print(L.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
print(L.findDuplicates([1, 1, 2]))
print(L.findDuplicates([1]))
