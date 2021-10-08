class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []

        def movements(node):
            if not node:
                return
            movements(node.left)
            answer.append(node.val)
            movements(node.right)

        movements(root)
        return answer