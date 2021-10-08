class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current = root
        while current:
            if current.val == val:
                return current
            elif val > current.val:
                current = current.right #bst esta ordenado derecha mayores
            else:
                current = current.left