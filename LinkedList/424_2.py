#
# 给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
#
# 你应当 保留 两个分区中每个节点的初始相对位置。Definition for singly-linked list.
链表断尾，否则OOM
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        minDummy = ListNode(0,None)
        maxDummy = ListNode(0,None)
        left = minDummy
        right = maxDummy
        temp = head
        while temp:
            if temp.val < x:
                left.next = temp
                left = left.next
            else:
                right.next = temp
                right = right.next
            temp = temp.next
        left.next = maxDummy.next
        right.next = None
        return minDummy.next
