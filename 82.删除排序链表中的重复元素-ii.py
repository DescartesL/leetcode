#
# @lc app=leetcode.cn id=82 lang=python
#
# [82] 删除排序链表中的重复元素 II
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
        dummy = ListNode(0)
        #prev保存current前一个元素，current保存当前元素
        prev,current,dummy.next = dummy,head,head

        while current and current.next:
            #current 和 current.next 值相等，那么存储这个值 temp 后往后找到第一个不相等的值，链接 prev 和 current
            if current.val == current.next.val:
                temp = current.val
                while current and current.val == temp:
                    current = current.next
                prev.next = current
            #两者不相等的时候，同时往后走
            else:
                current = current.next
                prev = prev.next
        
        return dummy.next
                



# @lc code=end

