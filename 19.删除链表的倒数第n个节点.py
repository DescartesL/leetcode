#
# @lc app=leetcode.cn id=19 lang=python
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #递归
        global count
        if head is None:
            count = 0
            return None
        
        head.next = self.removeNthFromEnd(head.next,n)
        count += 1
        return head.next if n==count else head
# @lc code=end 

