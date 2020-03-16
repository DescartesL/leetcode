

#
# @lc app=leetcode.cn id=142 lang=python
#
# [142] 环形链表 II
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast,slow = head,head
        #第一遍，两者等待第一次相遇
        while True :
            if not (fast and fast.next): return
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        fast = head
        #第二遍，两者相遇时即为环的起点
        while fast != slow:
            fast = fast.next
            slow = slow.next
                
        return fast
             
# @lc code=end

