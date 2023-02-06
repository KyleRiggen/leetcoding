class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []

        # :n operator 
        # zip built in function:
        # x = (zip(nums[:n],nums[n:]))
        # bundles 

        for i, j in zip(nums[:n],nums[n:]):
            res += [i,j]
        return res