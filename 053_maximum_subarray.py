# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        sums = 0

        # base base
        if max(nums) <= 0:
            return max(nums)

        # for the case there is at least one element which is larger than 0
        for i in range(len(nums)):
            if sums + nums[i] > 0:
                sums += nums[i]
            else:
                sums = 0
            ans = max(ans, sums)

        return ans

if __name__ == "__main__":
    nums = [-2, -1, -3, -4, -1, -2, -1, -5, -4]

    print(Solution().maxSubArray(nums))
