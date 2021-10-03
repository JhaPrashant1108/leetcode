class Solution:
    def dfs(self, grid, subset, last, partial, target, used):
        if subset == 1:
            return True
        if partial == target:
            return self.dfs(grid, subset-1, 0, 0, target, used)
        for i in range(last, len(grid)):
            if not used[i] and partial+grid[i] <= target:
                used[i] = True
                if self.dfs(grid, subset, i+1, partial+grid[i], target, used):
                    return True
                used[i] = False

    def canPartitionKSubsets(self, nums, k):
        nums.sort(reverse=True)
        numb = sum(nums)//k
        if(len(nums) == 0 or k == 0 or sum(nums) % k != 0 or nums[0] > numb):
            return False

        used = [False]*len(nums)
        return self.dfs(nums, k, 0, 0, numb, used)


L = Solution()

print(L.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))
print(L.canPartitionKSubsets([1, 2, 3, 4], 3))
