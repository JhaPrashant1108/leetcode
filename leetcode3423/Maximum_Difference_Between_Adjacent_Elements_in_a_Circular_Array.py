class Solution:
    def maxAdjacentDistance(self, nums):
        """
        Function to calculate the maximum absolute difference between adjacent elements
        in a circular array.
        """
        if not nums or len(nums) < 2:
            return 0

        res = abs(nums[0] - nums[-1])
        for i in range(len(nums) - 1):
            res = max(res, abs(nums[i] - nums[i + 1]))
        return res


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums1 = [1, 2, 4]
    result1 = solution.maxAdjacentDistance(nums1)
    print(f"Input: {nums1}")
    print(f"Output: {result1}")
    print("Expected: 3")
    print()

    # Example 2
    nums2 = [-5, -10, -5]
    result2 = solution.maxAdjacentDistance(nums2)
    print(f"Input: {nums2}")
    print(f"Output: {result2}")
    print("Expected: 5")