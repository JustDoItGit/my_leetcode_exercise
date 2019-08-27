class Solution:
    def hasCycle(self, head):
        nodesSeen = set()
        while head is not None:
            if head in nodesSeen:
                return True
            else:
                nodesSeen.add(head)
            head = head.next
        return False
