# You're given strings J representing the types of stones that are jewels,
# and S representing the stones you have.
# Each character in S is a type of stone you have.
# You want to know how many of the stones you have are also jewels.

import collections

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        counter = collections.Counter(S)
        count = 0

        for j in J:
            count += counter[j]

        return count

if __name__ == "__main__":
    J = "aA"
    S = "aDDAAabb"
    print(Solution().numJewelsInStones(J, S))
