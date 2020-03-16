#
# @lc app=leetcode.cn id=206 lang=python
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        result = None
        current = head
        while current :
            temp = current.next
            current.next = result
            result = current
            current = temp
        
        return result 

# @lc code=end

