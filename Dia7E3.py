class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        start = ListNode(0)
        start.next = head

        actualnode = head
        previousnode = start

        while actualnode:
            if actualnode.val == val:
                previousnode.next = actualnode.next
                actualnode = actualnode.next
            else:
                previousnode = actualnode
                actualnode = actualnode.next

        return start.next