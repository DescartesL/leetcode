#
# @lc app=leetcode.cn id=203 lang=python
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head
        while current:
            if current.val == val:
                prev.next = current.next 
                current = current.next
            else:
                prev = prev.next
                current = current.next
        return dummy.next
# @lc code=end

