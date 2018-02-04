class Solution(object):
    def twoSum(self, nums, target):
        """
        Using hash table to find the indices:
        Time complexity: O(n)
        Space complexity: O(1)

        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hash_dict = {}
        for index, num in enumerate(nums):
            if num in hash_dict:
                return [hash_dict[num], index]
            hash_dict[target-num] = index

"""
class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
"""

if __name__ == "__main__":
    nums = [3, 3, 2, 4, 10]
    target = 6
    print(Solution().twoSum(nums, target))
