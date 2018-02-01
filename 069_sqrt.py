class Solution:
    def mySqrt(self, x):
        """
        using binary search algorithm to calculate the square root of integer x
        time complexity: O(log n)
        space complexity: O(1)

        :type x: int
        :rtype: int
        """

        # base case
        if(x == 0 or x == 1):
            return x

        start = 1
        end   = x
        while(start <= end):
            mid = (start + end) // 2
            if(mid * mid == x):
                return mid
            elif(mid * mid < x):
                start  = mid + 1
                result = mid
            else:
                end = mid - 1

        return result

if __name__ == "__main__":
    print(Solution().mySqrt(8))
