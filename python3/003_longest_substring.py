# Given a string, find the length of the longest substring without repeating characters.


# # 1. Brute force method: time limit exceeded. O(n^3)
# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if len(s) <= 0:
#             return 0
#         if len(s) == 1:
#             return 1
#         ans = 0
#         for i in range(len(s)-1):
#             for j in range(i, len(s)):
#                 if self.allUnique(s, i, j):
#                     ans = max(ans, j-i+1)
#
#         return ans
#
#     def allUnique(self, s, start, end):
#         lists = []
#         for i in range(start, end+1):
#             if s[i] in lists:
#                 return False
#
#             lists.append(s[i])
#
#         return True

from collections import defaultdict

# 2. Sliding window
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        low, high, ans = 0, 0, 0
        s_dict = defaultdict(int)

        while high < len(s):
            letter = s[high]
            if letter in s_dict:
                low = max(s_dict[letter] + 1, low)
                # print("low: ", low)
                s_dict[letter] = high
            else:
                s_dict[letter] = high
            # print("s_dict: ", s_dict)
            high += 1
            ans = max(ans, high - low)

        return ans


if __name__ == '__main__':
    s = "abba"

    print(Solution().lengthOfLongestSubstring(s))
