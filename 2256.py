class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            retur
            n 0

        queue = deque(nums[1:])

        left_sum = sum(nums[0: 1])
        right_sum = sum(queue)

        left_length = 1
        right_length = n - 1

        i = 0

        min_avg = sys.maxsize
        min_avg_idx = None

        while i < n:
            left_avg = left_sum // left_length
            if right_length:
                right_avg = right_sum // right_length
            else:
                right_avg = 0

            diff = abs(left_avg - right_avg)
            if diff < min_avg:
                min_avg = diff
                min_avg_idx = i

            # if queue is empty, we can stop. as it is the end.
            if not queue:
                break
            # remove ele from left of the queue
            element = queue.popleft()

            # update for next iteration
            left_sum = left_sum + element
            right_sum = right_sum - element

            left_length += 1
            right_length -= 1

            i += 1

        return min_avg_idx
