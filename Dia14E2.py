class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        values = set()

        def looksum(node):
            if not node:
                return False
            rest = k - node.val
            if rest in values:
                return True
            else:
                values.add(node.val)
            return looksum(node.left) or looksum(node.right)

        return looksum(root)