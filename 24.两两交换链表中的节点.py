#
# @lc app=leetcode.cn id=24 lang=python
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # def reverseList(node):
        # if node is  None or node.next is  None:
        #     return node
        # p = self.reverseList(node.next)
        # node.next.next = node.next
        # node.next = None
        # return p
        
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #出口条件Base
        if head is None or head.next is None:
            return head

        #交换
        first =  head
        second = head.next
        first.next = self.swapPairs(second.next) 
        second.next = first
        return second
        
# @lc code=end

