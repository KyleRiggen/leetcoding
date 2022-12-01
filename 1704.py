vowels = "aeiouAEIOU"

class Solution:

    # S is word given, bool means function will return a boolean only
    def halvesAreAlike(self, S: str) -> bool:

        # // is floor division
        # mid is finding middle of word
        # ans is set to zero, to be increased later
        mid, ans = len(S) // 2, 0

        # range(start, stop, step) starting at middle of word
        for i in range(mid):

            # increase answer if specific letter is a vowel
            if S[i] in vowels: ans += 1

            # decrease answer if specific letter on same side of word is a vowel
            if S[mid+i] in vowels: ans -=1
        
        # return true if answer is 0, so each side has matching vowels
        # otherwise return fasle if answer is not zero
        return ans == 0
