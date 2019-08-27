class Solution:
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if slow is None or fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

    def hasCycle2(self, head):
        fast = slow = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
