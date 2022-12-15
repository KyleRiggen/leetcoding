class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # store the lengths of the two texts
        n = len(text1)
        m = len(text2)

        # we create a list dp such that dp[i][j] will represent
        # the LCS between text1[:i+1] and text2[:j+1]
        dp = [[0] * m for _ in range(n)]

        # iterate through all the indices of dp
        for i in range(n):
            for j in range(m):
                # if the two characters we are looking at are the same
                if text1[i] == text2[j]:
                    # the LCS between text1[:i+1] and text2[:j+1] is one more
                    # than the LCS between text1[:i] and text2[:j]
                    dp[i][j] = 1 + (i > 0 and j > 0 and dp[i - 1][j - 1])
                else:  # otherwise
                    # the LCS between text1[:i+1] and text2[:j+1] is the max of the
                    # LCS between text1[:i+1] and text2[:j] and the
                    # LCS between text1[:i] and text2[:j+1]
                    dp[i][j] = max(((i > 0 and dp[i - 1][j]) or 0), ((j > 0 and dp[i][j - 1]) or 0))

        # return the LCS between the full strings
        return dp[-1][-1]