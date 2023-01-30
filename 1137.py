class Solution:
    def tribonacci(self, n: int) -> int:
        lst = [0, 1, 1]
        if n < 2:
            return lst[n]
        else:
            for i in range(n-2):
                lst.append(sum(lst))
                lst.pop(0)
        return lst.pop()