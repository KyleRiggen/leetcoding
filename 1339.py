# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def helper(curr):
            if curr is None:
                return 0
            curr.val += helper(curr.left) + helper(curr.right)
            return curr.val

        sumnum = helper(root)

        curr = root
        ans = 0
        while curr is not None and curr.val >= sumnum / 2:
            another = sumnum - curr.val
            ans = max(ans, another * curr.val)
            left = right = 0
            if curr.left is not None:
                left = curr.left.val
            if curr.right is not None:
                right = curr.right.val
            if left > right:
                curr = curr.left
            else:
                curr = curr.right
        if curr is None:
            return ans
        newans = curr.val * (sumnum - curr.val)
        return max(newans, ans) % (pow(10, 9) + 7)