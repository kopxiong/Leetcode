# Given a string s, find the longest palindromic substring in s.

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""

        if (len(s) < 2):
            return s
        for i in range(len(s)):
            temp = self.helper(s, i, i)
            if len(temp) > len(result):
                result = temp

            temp = self.helper(s, i, i+1)
            if len(temp) > len(result):
                result = temp

        return result


    def helper(self, s, left, right):
        while (left >= 0 and right < len(s) and s[left] == s[right]):
            left = left - 1
            right = right + 1

        return s[left+1: right]


if __name__ == '__main__':
    s = "helloworld"

    print(Solution().longestPalindrome(s))
