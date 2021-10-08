class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        def movements(node):
            if not node:
                return
            movements(node.left)
            movements(node.right)
            answer.append(node.val)
        movements(root)
        return answer