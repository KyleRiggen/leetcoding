class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.result = 0
        def dfs(node, curr_sum):
            if not node:
                return
            curr_sum = curr_sum * 10 + node.val
            if not node.left and not node.right:
                self.result += curr_sum
                return
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)

        dfs(root, 0)
        return self.result