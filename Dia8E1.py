class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        actualnode = head

        while actualnode:
            mov = actualnode.next
            actualnode.next = prev
            prev = actualnode
            actualnode = mov

        return prev