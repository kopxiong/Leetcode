# Find the kth largest element in an unsorted array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

import random

class Solution:
    # def findKthLargest(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: int
    #     """
    #     if len(nums) < k:
    #         return -1
    #
    #     return sorted(nums)[::-1][k-1]

    def findKthLargest1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        # To avoid the worst case
        random.shuffle(nums)
        while low <= high:
            pIndex = self.partition(nums, low, high)
            if k < pIndex + 1:
                high = pIndex - 1
            elif k > pIndex + 1:
                low = pIndex + 1
            else:
                return nums[pIndex]

    def partition(self, nums, start, end):
        pIndex = start
        pivot = nums[end]
        for i in range(start, end):
            if nums[i] > pivot:
                nums[i], nums[pIndex] = nums[pIndex], nums[i]
                pIndex += 1
        nums[end], nums[pIndex] = nums[pIndex], nums[end]

        return pIndex

if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 3

    print(Solution().findKthLargest1(nums, k))
