import java.util.Arrays;

class Solution {
    public int maxAdjacentDistance(int[] nums) {
        if (nums == null || nums.length < 2) {
            return 0;
        }
        int res = Math.abs(nums[0] - nums[nums.length - 1]);

        for (int i = 0; i < nums.length - 2; i++) {
            res = Math.max(res, Math.abs(nums[i] - nums[i + 1]));
        }
        return res;
    }
}

public class Maximum_Difference_Between_Adjacent_Elements_in_a_Circular_Array {

    public static void main(String[] args) {

        Solution solution = new Solution();

        // Example 1
        int[] nums1 = { 1, 2, 4 };
        int result1 = solution.maxAdjacentDistance(nums1);
        System.out.println("Input: " + Arrays.toString(nums1));
        System.out.println("Output: " + result1);
        System.out.println("Expected: 3");
        System.out.println();

        // Example 2
        int[] nums2 = { -5, -10, -5 };
        int result2 = solution.maxAdjacentDistance(nums2);
        System.out.println("Input: " + Arrays.toString(nums2));
        System.out.println("Output: " + result2);
        System.out.println("Expected: 5");
    }
}
