class Solution:
    def search(self, nums, target):
        if not nums or len(nums) == 0:
            return -1
        l, r = 0, len(nums) - 1
        while(l < r):
            mid = (int)(l + (r-l)/2)
            if (nums[mid] > nums[r]):
                l = mid+1
            else:
                r = mid
        start = l
        l, r = 0, len(nums)-1
        if target >= nums[start] and target <= nums[r]:
            l = start
        else:
            r = start
        while(l <= r):
            mid = (int)(l + (r-l)/2)
            if nums[mid] == target:
                return mid
            elif(nums[mid] < target):
                l = mid+1
            else:
                r = mid - 1
        return -1


L = Solution()
print(L.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
print(L.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
print(L.search(nums=[1], target=0))
