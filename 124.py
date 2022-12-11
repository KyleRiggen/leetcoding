# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsum = [float('-inf')]

        def helper(root, maxsum):
            if not root: return 0
            left = helper(root.left, maxsum)
            right = helper(root.right, maxsum)
            temp = max(root.val, root.val + left, root.val + right)
            maxsum[0] = max(temp, root.val + left + right, maxsum[0])

            return temp

        helper(root, maxsum)
        return maxsum[0]