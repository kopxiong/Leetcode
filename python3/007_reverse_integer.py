# Given a 32-bit signed integer, reverse digits of an integer.

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Solution1:
        # n = int(str(abs(x))[::-1])
        # return 0 if x == 0 else ((x>0)-(x<0)) * n * (n < 2**31)

        # Solution2:
        # sign = -1 if x < 0 else 1
        # x *= sign
        #
        # while x:
        #     if x % 10 == 0:
        #         x /= 10
        #     else:
        #         break
        # x = list(str(x))
        # x = int("".join(x[::-1]))
        #
        # if (-(1 << 31) <= x <= (1 << 31) - 1):
        #     return x*sign
        # else:
        #     return 0

        # Solution3:
        if x >= 0:
            val = int(str(x)[::-1])
        else:
            val = -int(str(-x)[::-1])

        if (-2 ** 31) <= val <= (2 ** 31 - 1):
            return val
        else:
            return 0

if __name__ == '__main__':
    x = 1534236469

    print(Solution().reverse(x))
