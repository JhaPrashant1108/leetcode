class Solution:
    def twoSum(self, nums, target):
        compliments = {}
        result = []
        for index,num in enumerate(nums):
            if compliments.get(num) is None:
                compliments[target-num] = index
            else:
                result = [compliments[num],index]
        return result

l = Solution()

print(l.twoSum([],54))
print(l.twoSum([2,1,3],4))
