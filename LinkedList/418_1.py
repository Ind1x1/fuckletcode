# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        length = 1
        while temp.next != None:
            length += 1
            temp = temp.next
        i = 0
        deleten = length - n
        if deleten == 0:
            return head.next
        temp = head
        for _ in range(deleten-1):
            temp = temp.next
        temp.next = temp.next.next
        return head