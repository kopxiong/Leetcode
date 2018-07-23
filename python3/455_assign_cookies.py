# Assume you are an awesome parent and want to give your children some cookies.
# But, you should give each child at most one cookie. Each child i has a greed factor gi,
# which is the minimum size of a cookie that the child will be content with;
# and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i,
# and the child i will be content.
# Your goal is to maximize the number of your content children and output the maximum number.

class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        ans = 0

        g.sort(reverse=True)
        s.sort(reverse=True)
        i = j = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                ans += 1
                i += 1
                j += 1
            else:
                i += 1

        return ans

if __name__ == '__main__':
    g = [1, 2]
    s = [1, 2, 3]
    print(Solution().findContentChildren(g, s))
