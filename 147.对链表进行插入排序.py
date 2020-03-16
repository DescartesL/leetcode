#
# @lc app=leetcode.cn id=147 lang=python
#
# [147] 对链表进行插入排序
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head


        dummy = ListNode(0)
        current = dummy.next = head


        while current and current.next:
            if current.val <= current.next.val:
                current = current.next
            else:
                temp = current.next #存储current的下一个元素
                current.next = current.next.next
                pre = dummy


                while pre.next.val <= temp.val:
                    pre = pre.next
                
                temp.next = pre.next
                pre.next = temp
        return dummy.next




# @lc code=end




# @lc code=end

