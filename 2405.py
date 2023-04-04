class Solution:
    def partitionString(self, s: str) -> int:

        # new syntax:
        # Return the integer that represents the character "h":
        # x = ord("h")
        # so converting alphabetical letters to numbers to be able to flow through the entire alphabet

        # create array with size 26, to be filled with -1
        lastSeen = [-1]*26

        # create count variable to keep track of number of substrings formed
        count = 1

        # integer variable to hold the starting index of the substring under consideration
        substringStarting = 0

        # iterate over the input string "s"
        for i in range(len(s)):

            # if the most recent position s[i] is greater than or equal to
            # the starting position of the substring,
            # it means we have already included this character
            # so we increase "count" by 1 as we start a new substring and
            # set "substringStarting" to "i"
            if lastSeen[ord(s[i]) - ord('a')] >= substringStarting:
                count += 1
                substringStarting = i

            # update lastSeen for the current character
            lastSeen[ord(s[i]) - ord('a')] = i

        return count