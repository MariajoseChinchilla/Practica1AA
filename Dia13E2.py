class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        def insert(node, val):
            if val > node.val:
                if not node.right:
                    node.right = TreeNode(val)
                insert(node.right, val)
            if val < node.val:
                if not node.left:
                    node.left = TreeNode(val)
                insert(node.left, val)

        insert(root, val)

        return root