class Solution:
    def rob(self, nums: List[int]) -> int:
        h1,h2 = 0,0
        for n in nums:  # h1,h2,h3,h4,...h_n
            h_n = max(n+h1,h2)
            h1 = h2
            h2 = h_n
        return h_n