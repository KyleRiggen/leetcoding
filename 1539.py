class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        # n = 5
        n = len(arr)
        print(f"n: {n}")

        start, end = 0, n-1
        print(f"start: {start}")
        print(f"end: {end}")


        while start <= end:

            # // floor division
            # mid = 0 + (4 - 0) // 2 = 2
            mid = start + (end - start) // 2
            print(f"mid: {mid}")

            print(f"wtf: {arr[mid] - (mid + 1)}")
            if arr[mid] - (mid + 1) < k:
                start = mid + 1
            else:
                end = mid - 1
        return start + k