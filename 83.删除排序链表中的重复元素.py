#
# @lc app=leetcode.cn id=83 lang=python
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #creat 两个标记，标记当前位置和下一个位置，若两个元素相等，那么跳过下一个，若不相等，那么两者同时后移
        dummy = ListNode(-1)
        exp , cur ,dummy.next = head,head,head
        
        while exp is not None:
            if cur.val == exp.val:
                cur.next = exp.next
                exp = cur.next
            else:
                cur,exp = cur.next,exp.next
        
        return dummy.next
# @lc code=end

