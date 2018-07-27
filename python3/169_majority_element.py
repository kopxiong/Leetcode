# Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Binary search: Time complexity: O(N); Space complexity: O(N) (call stack)

import collections

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # NO.1: using countingSort, but has memory error (nums = [-1, -1, 2147483647])
        # count = [0] * (max(nums) - min(nums) + 1)
        # for index in nums:
        #     count[index - min(nums)] += 1
        #
        # majority_index = [index for index in range(len(count)) if count[index] == max(count)]
        #
        # return min(nums) + majority_index[0]


        # NO. 2: Hashmap
        # counts = collections.Counter(nums)
        #
        # return max(counts.keys(), key=counts.get)  # not return counts.get(max(counts.keys()))

        # NO. 3: Divide and Conquer
        def divide_and_conquer(low, high):
            # base case
            if low == high:
                return nums[low]

            middle = (high - low) // 2 + low
            left = divide_and_conquer(low, middle)
            right = divide_and_conquer(middle+1, high)

            # if left and right is consistent
            if left == right:
                return left

            # else, return the winner of the majority
            left_count = sum(1 for i in range(low, high+1) if nums[i] == left)
            right_count = sum(1 for i in range(low, high+1) if nums[i] == right)

            return left if left_count > right_count else right

        return divide_and_conquer(0, len(nums)-1)


if __name__ == "__main__":
    nums = [-1, -1, 2147483647]

    print(Solution().majorityElement(nums))
