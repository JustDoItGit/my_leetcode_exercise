class Solution:
    def swapPairs(self, head):
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            # pre.next 指向 b， 防止链表丢掉两两交换后的第一个节点
            pre.next, b.next, a.next = b, a, b.next  # 这里的一次性赋值，动作全部都是指向
            pre = a
        return self.next  # 结果要求返回的是链表第一个元素head
