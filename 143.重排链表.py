
#
# @lc app=leetcode.cn id=143 lang=python
#
# [143] 重排链表
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        #1,找到中点位置，把后面的元素组成的链表进行逆序，然后再将两个链表依次连接起来
        if not (head and head.next):
            return


        #快慢指针找到中点
        slow,fast = head,head
        while  fast.next:
            slow,fast = slow.next,fast.next
            if not fast.next:
                break
            fast = fast.next
        
        mid = slow


        #反转后面的链表
        prev = None
        while slow:
            temp = slow.next
            slow.next  = prev
            prev = slow
            slow = temp
        
        latter = prev #新链表


        #插入操作
        cur = head
        while latter != mid:
            temp1 = cur.next
            cur.next = latter
            temp2 = latter.next
            latter.next = temp1
            cur = temp1
            latter = temp2
        
        return head
                
        
# @lc code=end

