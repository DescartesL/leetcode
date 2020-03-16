#
# @lc app=leetcode.cn id=61 lang=python
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        cur = dummy.next = head
        fast = slow = dummy
        n = 0#计数
        
        #统计链表个数
        while cur:
            cur,n  = cur.next,n+1
        
        #当n为0或者k为n的整倍数
        if n == 0 or k % n == 0:
            return head
        
        #k可能会大于n
        n = k % n
        #快指针先走
        while fast.next is not None and n > 0:
            fast,n = fast.next, n-1
        
        while fast.next is not None:
            slow,fast = slow.next,fast.next
        
        fast.next = head
        dummy.next =  slow.next
        slow.next = None

        return dummy.next

# @lc code=end

