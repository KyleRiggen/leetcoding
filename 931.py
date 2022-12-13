class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        cols = len(matrix[0])

        ans = matrix[0].copy()
        prev = matrix[0].copy()

        # loop for 1st set
        for row in range(1, len(matrix)):

            # loop for 2nd set
            for i in range(cols):

                #
                if i == 0:
                    if cols > 1:
                        prev_min = min(prev[i], prev[i + 1])
                    else:
                        prev_min = min(prev[i])
                elif i == cols - 1:
                    prev_min = min(prev[i], prev[i - 1])
                else:
                    prev_min = min(prev[i], prev[i - 1], prev[i + 1])
                ans[i] = prev_min + matrix[row][i]
            prev = ans.copy()

        return min(ans)
