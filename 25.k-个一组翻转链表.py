#
# @lc app=leetcode.cn id=25 lang=python
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        p = dummy
        while True:
            count = k
            stack = []
            temp = head
            while temp and count:
                stack.append(temp)
                temp = temp.next
                count -= 1
            if count:
                p.next = head
                break
            while stack:
                p.next = stack.pop()
                p = p.next
            
            p.next = temp
            head = temp

        return dummy.next




# @lc code=end

