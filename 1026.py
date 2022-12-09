# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def find_max_difference(root, low, high):
            if not root:
                return high - low
            high = max(high, root.val)
            low = min(low, root.val)
            return max(find_max_difference(root.left, low, high), find_max_difference(root.right, low, high))

        # Check if the input root is None
        if not root:
            return 0
        else:
            return find_max_difference(root, root.val, root.val)