class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.ismirror(root.left, root.right)

    def ismirror(self, left, right):
        if left and right:
            return left.val == right.val and self.ismirror(left.left, right.right) and self.ismirror(left.right,
                                                                                                     right.left)

        return left == right