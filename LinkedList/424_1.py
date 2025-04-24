# 给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head

        while current:
            # 检查是否为重复节点
            if current.next and current.val == current.next.val:
                val_to_remove = current.val
                # 跳过所有相同值的节点
                while current and current.val == val_to_remove:
                    current = current.next
                prev.next = current
            else:
                prev = current
                current = current.next