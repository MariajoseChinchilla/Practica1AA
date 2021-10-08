class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        stack = []
        while root or stack:
            while root:
                answer.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return answer