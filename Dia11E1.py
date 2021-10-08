class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        q = collections.deque()
        q.append(root)

        while q:
            qlen = len(q)
            toadd = []
            for i in range(qlen):
                node = q.popleft()
                if node:
                    toadd.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if toadd != []:
                answer.append(toadd)
        return answer