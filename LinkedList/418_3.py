# 两两交换链表中的节点

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head and head.next:
            # 拿到两个要交换的节点
            first = head
            second = head.next

            # 开始交换
            prev.next = second
            first.next = second.next
            second.next = first

            # 移动指针准备下一对
            prev = first
            head = first.next

        return dummy.next