"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
#
# 给定一个二叉树：
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL 。
#
# 初始状态下，所有 next 指针都被设置为 NULL 。



class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        start = root
        while start:
            self.last = None
            self.nextStart = None
            p = start
            while p:
                if p.left:
                    self.handle(p.left)
                if p.right:
                    self.handle(p.right)
                p = p.next
            start = self.nextStart
        return root

    def handle(self, p):
        if self.last:
            self.last.next = p
        if not self.nextStart:
            self.nextStart = p
        self.last = p
