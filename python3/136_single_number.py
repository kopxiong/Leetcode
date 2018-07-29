# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Time complexity: O(N); Space complexity: O(1)

from collections import Counter

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = Counter(nums)

        return [k for k, v in count.items() if v == 1][0]


if __name__ == '__main__':
    nums = [1, 2, 4, 5, 2, 1, 5]

    print(Solution().singleNumber(nums))
