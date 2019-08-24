class Solution:
    def reverseList(self, head):
        cur, prev = head, None
        while cur:
            """
            nextTemp = cur.next
            cur.next = prev
            prev = cur
            cur = nextTemp
            """
            cur.next, prev, cur = prev, cur, cur.next
        return prev
