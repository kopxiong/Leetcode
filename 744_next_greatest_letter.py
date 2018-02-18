# Given a list of sorted characters letters containing only lowercase letters,
# and given a target letter, find the smallest element in the list that is larger than the given target.

# Letters also wrap around. For example,
# if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

# Algorithm: binary search, time complexity: O(log n)

import bisect
import random
import string


class Solution:
    def nextGreatestLetter1(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """

        if target >= letters[len(letters)-1]:    # consider wrap case
            return letters[0]
        else:
            return next(x for x in letters if x > target)

    # using bisect.bisect_right
    def nextGreatestLetter2(self, letters, target):
        return letters[bisect.bisect_right(letters, target) % len(letters)]


if __name__ == "__main__":
    length = 10
    letters = random.sample(string.ascii_lowercase[0:26], length)
    letters.sort()
    target  = random.choice(string.ascii_lowercase[0:26])
    print("letters: ", letters)
    print("target: ", target)
    print("result1: ", Solution().nextGreatestLetter1(letters, target))
    print("result2: ", Solution().nextGreatestLetter2(letters, target))
