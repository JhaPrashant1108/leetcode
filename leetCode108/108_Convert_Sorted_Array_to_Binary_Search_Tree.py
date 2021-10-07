class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeMaker(self, nums, left, right):
        if left > right:
            return
        mid = (int)(left + (right - left)/2)
        node = TreeNode(nums[mid])
        node.left = self.treeMaker(nums, left, mid-1)
        node.right = self.treeMaker(nums, mid+1, right)

        return node

    def sortedArrayToBST(self, nums):
        if not nums:
            return
        return self.treeMaker(nums, 0, len(nums)-1)


L = Solution()
print(L.sortedArrayToBST([-10, -3, 0, 5, 9]))
print(L.sortedArrayToBST([1, 3]))
