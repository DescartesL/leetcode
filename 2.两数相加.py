#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def addhelper(a,b,doc):
            if not (a or b):
                return ListNode(1) if doc else None

            #防止两个链表长度不一样，所以如果其中一个为None时要在后面补0节点    
            a = a if a else ListNode(0)
            b = b if b else ListNode(0)
            val = a.val + b.val + doc
            doc = 1 if val >= 10 else 0
            a.val = val % 10
            a.next = addhelper(a.next,b.next,doc)
            return a
        return addhelper(l1,l2,0)




        
# @lc code=end

