class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        '''
        Using example scores = [1,2,3,5] and ages = [8,9,10,1]

        data is   [(1, 5), (8, 1), (9, 2), (10, 3)]
        and dp is [5, 1, 2, 3]

        when curr player is (1, 5)
            there are no prev players -> so leave dp of curr as-is

        when curr player is (8, 1)
            prev player's score is not less than curr player score
            nor is previous player's age same as curr player age -> so leave dp of curr as-is

        when curr player is (9, 2)
            prev player (1, 5) has score NOT less than, and age NOT equal to ... skipping
            prev player (8, 1) has score YES less than ... so we do something!
                since the accumulated dp of prev player + curr's score is GREATER than curr's accumulated dp value:
                    we update curr's accumulated dp value to be instead sum of prev player's dp value and curr's score

        when curr player is (10, 3)
            prev player (1, 5) has score NOT less, and age NTO equal to ... skipping
            prev player (8, 1) has score YES less, so update curr's dp value from 3 -> 3+1 = 4
            prev player (9, 2) has score YES less, so update curr's dp value from 4 -> 4+2 = 6

        finally we return the max of all dp values for the dream team.
        '''
        # Sort by age and score ASC
        data = sorted(zip(ages, scores), key=lambda x: (x[0], x[1]))
        # Initialize dp with scores for each player
        dp = [score for age, score in data]
        N = len(data)

        # For every current player
        for curr in range(N):
            # Compare every previous player
            for prev in range(0, curr):
                # And if previous player score is less OR previous player is same age
                if (data[prev][1] <= data[curr][1] or data[curr][0] == data[prev][0]):
                    # Then update dp value for current player to be the max of either
                    #  -> the current score as it is OR
                    #  -> the current score PLUS the dp value of previous player
                    dp[curr] = max(dp[curr], data[curr][1] + dp[prev])

        return max(dp)
