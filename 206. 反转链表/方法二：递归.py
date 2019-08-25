class Solution:
    def reverseList(self, head):
        if head is None or head.next is None:  # 空链或只有一个结点，直接返回头指针
            return head
        # 有两个以上结点
        p = self.reverseList(head.next)  # 反转以第二个结点为头的子链表
        # head->next 此时指向子链表的最后一个结点
        # 将之前的头结点放入子链尾
        head.next.next = head
        head.next = None
        return p
