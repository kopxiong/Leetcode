# Given a sorted array and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# Assume no duplicates in the array.

# Algorithm: binary search, time complexity: O(log n)
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        '''
        # base case
        if target > nums[len(nums) - 1]:
            return len(nums)
        if target < nums[0]:
            return 0
        '''
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2       # mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        return left

'''
# Algorithm1: binary search in python
import bisect

class Solution1(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return bisect.bisect_left(nums, target)
'''

if __name__ == "__main__":
    nums = [1, 2, 5, 6]
    target = 7
    print(Solution().searchInsert(nums, target))
