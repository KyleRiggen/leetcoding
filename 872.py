class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def leaf(root):
            if root.left or root.right:
                if root.left:
                    for key in leaf(root.left):
                        yield key
                if root.right:
                    for key in leaf(root.right):
                        yield key
            else:
                yield root.val
        return list(leaf(root1)) == list(leaf(root2))