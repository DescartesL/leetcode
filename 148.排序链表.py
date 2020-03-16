#
# @lc app=leetcode.cn id=148 lang=python
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getMid(self,head):
        if not (head and head.next):
            return head
        
        pre, slow,fast = head,head.next,head.next
        while fast and fast.next:
            pre,slow,fast= slow,slow.next,fast.next.next
        
        pre.next = None
        return slow

    def merge(self,left,right):
        res = ListNode(-1)
        pre = res
        while left and right:
            if left.val <= right.val:
                pre.next = left
                left = left.next
            else:
                pre.next = right
                right = right.next
            pre = pre.next

        pre.next = left if left else right
        return res.next

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not (head and head.next):
            return head

        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left,right)
    
            


# @lc code=end

