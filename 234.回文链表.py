#
# @lc app=leetcode.cn id=234 lang=python
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #思路：找到链表的中点，分成两个链表，然后逆置后一个链表，再对两个链表进行比较、
        if not (head and head.next):
            return True

        dummy = ListNode(-1)
        dummy.next,slow , fast = head , dummy, dummy
        #找到中点
        while fast and fast.next:
            slow,fast = slow.next,fast.next.next

        reslult = None
        current = slow.next
        slow.next = None
        #逆置后面的链表
        
        while current:
            temp = current.next
            current.next = reslult
            reslult = current
            current = temp
        
        #比较两个链表
        first ,second = dummy.next,reslult
        while second:#这里只需要判断后面一个链表即可，否则就会报错，因为first and second的时候如果是偶数就会出问题
            if first.val != second.val:
                return False
            else:
                first = first.next
                second = second.next
        return True

# @lc code=end

