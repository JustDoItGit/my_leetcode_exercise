class Solution:
    def hasCycle(self, head):
        """
        此方法不保险，存在val本来就有值为：bjfuvth'的情况
        """
        while head:
            if head.val == 'bjfuvth':
                return True
            else:
                head.val = 'bjfuvth'
            head = head.next
        return False
