# 给你单链表的头指针
# head
# 和两个整数
# left
# 和
# right ，其中
# left <= right 。请你反转从位置
# left
# 到位置
# right
# 的链表节点，返回
# 反转后的链表 。

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # 1. 找到 left 节点的前一个节点 prev
        for _ in range(left - 1):
            prev = prev.next

        # 2. 反转从 prev.next 开始的 right-left+1 个节点
        curr = prev.next
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next