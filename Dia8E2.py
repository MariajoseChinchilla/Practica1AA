class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        actualnode = head
        while actualnode and actualnode.next:
            if actualnode.val == actualnode.next.val:
                actualnode.next = actualnode.next.next
            else:
                actualnode = actualnode.next
        return head