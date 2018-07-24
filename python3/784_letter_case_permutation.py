# Given a string S, we can transform every letter individually to be
# lowercase or uppercase to create another string.
# Return a list of all possible strings we could create.

import itertools

class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        ## 1.
        # ans = [[s.lower(), s.upper()] if s.isalpha() else s for s in S]
        #
        # # star * is used to unpack a list
        # return [''.join(i) for i in itertools.product(*ans)]

        ## 2. DFS (Depth First Search)
        ans = []
        def dfs(S, i, n):
            if i == n:
                ans.append(''.join(S))
                return

            dfs(S, i+1, n)
            if not S[i].isalpha():
                return
            S[i] = chr(ord(S[i]) ^ (1<<5))
            dfs(S, i+1, n)
            S[i] = chr(ord(S[i]) ^ (1<<5))

        dfs(list(S), 0, len(S))

        return ans


if __name__ == "__main__":
    S = "a1b2"

    print(Solution().letterCasePermutation(S))
