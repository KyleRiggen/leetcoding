class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        """
        We have three states:
            - s0: starting state, no stock, can rest or buy
            - s1: just bought stock, can rest or sell
            - s2: just sold stock, must rest

        The reason state s2 exists is that we want to force a rest between leaving s1 (previous sell) and s0 (next buy).

        Each state has the following actions:
            - s0:
                - s0 -> s0: no stock, rest
                - s0 -> s1: buy new stock
            - s1:
                - s1 -> s1: hold stock, rest
                - s1 -> s2: sell stock
            - s2:
                - s2 -> s0: forced rest

        Let sk[j], k = {0, 1, 2}, j = {0, 1, ..., n}, denote the profit at state sk on day j
        (e.g., s1[2] is the profit on day 2 if we happened to be there).

        We have the following ways to enter each state:
            - Entering s0[i]:
                - From s0[i-1]: rest on day i, so profit remains the same as s0[i-1]
                - From s2[i-1]: forced rest on day i, so profit remains the same as s2[i-1]
            - Entering s1[i]:
                - From s1[i-1]: rest on day i, so profit remains the same as s1[i-1]
                - From s0[i-1]: bought stocks on day i, so profit is updated to (s0[i-1]-profits[i])
            - Entering s2[i]:
                - From s1[i-1]: sold stock on day i, so profit is updated to (s1[i-1]+profits[i])

        Initial states:
            - s[0] = 0: you start with 0 profit on day 0
            - s1[0] = -prices[0]: if you bought stock on day 0, ur profit is -prices[0]
            - s2[0] = X: dummy state as you need two days to buy and sell
        """

        n = len(prices)
        if not n:
            return 0

        s0, s1, s2 = [0] * n, [0] * n, [0] * n

        s0[0] = 0
        s1[0] = -prices[0]
        s2[0] = 0  # dummy

        for i in range(1, n):
            s0[i] = max(s0[i - 1], s2[i - 1])
            s1[i] = max(s1[i - 1], s0[i - 1] - prices[i])
            s2[i] = s1[i - 1] + prices[i]

        return max(s0[-1], s2[-1])