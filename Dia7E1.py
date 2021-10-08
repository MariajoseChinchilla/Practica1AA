class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        iterated = set()
        actual_node = head
        while actual_node:
            if actual_node in iterated:
                return True
            iterated.add(actual_node)
            actual_node = actual_node.next
        return False