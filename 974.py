class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        prefix_sum = 0
        sums = {0: 1}
        answer = 0
        for num in A:
            prefix_sum += num
            key = prefix_sum%K
            if key in sums:
                answer += sums[key]
                sums[key] += 1
                continue
            sums[key] = 1
        return answer