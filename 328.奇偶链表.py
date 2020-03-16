#
# @lc app=leetcode.cn id=328 lang=python
#
# [328] 奇偶链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not (head and head.next):
            return head

        odd = head
        temp = even = odd.next
        while even and even.next:
            odd.next,even.next = odd.next.next,even.next.next
            odd,even = odd.next,even.next
        
        odd.next = temp
        
        return head

# @lc code=end

