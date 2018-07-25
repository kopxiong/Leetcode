# Given an array that is definitely a mountain,
# return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

# Binary search: Time complexity: O(logN); Space complexity: O(1)

class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        left, right = 0, len(A) - 1

        while (left < right):
            middle = (left + right) // 2
            if (A[middle] < A[middle+1]):
                left = middle + 1
            else:
                right = middle

        return left

if __name__ == "__main__":
    A = [0, 2, 3, 4, 5, 3, 1, 0]

    print(Solution().peakIndexInMountainArray(A))
