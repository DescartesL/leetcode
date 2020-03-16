#
# @lc app=leetcode.cn id=160 lang=python
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        #headA和headB分别使用一个遍历的指针，当其中一个到达终点时换到另一个链表上。当两者相遇时即为所求
        pointA ,pointB = headA,headB
        while pointA != pointB:
            pointA = pointA.next if pointA else headB
            pointB = pointB.next if pointB else headA
        return pointA
        

# @lc code=end

