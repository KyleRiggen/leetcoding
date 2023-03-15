class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        end = False
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()

            if not node:
                end = True
            else:
                if end:
                    return False
                else:
                    queue.append(node.left)
                    queue.append(node.right)

        return True