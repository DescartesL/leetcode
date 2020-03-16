#
# @lc app=leetcode.cn id=86 lang=python
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        current = head 
        Smaller,Bigger = ListNode(0),ListNode(0)
        s,b = Smaller,Bigger
        while current:
            if current.val < x :
                s.next = current
                s = s.next
                current = current.next
            else:
                b.next = current
                b = b.next
                current = current.next
        b.next = None
        s.next = Bigger.next
        
        return Smaller.next 
            
# @lc code=end

