#
# @lc app=leetcode.cn id=445 lang=python
#
# [445] 两数相加 II
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
        def add(num1,num2,i,j):
            if not i or not j :
                return 0
            
            if num1 > num2:
                temp = i.val + add(num1-1,num2,i.next,j)
            #其实这里的else已经是等于的情况了
            else:
                temp = i.val + j.val + add(num1,num2,i.next,j.next)

            i.val = temp % 10
            
            return temp // 10
        #计算l1和l2的长度
        num1 = num2 = 0
        cur = l2
        while cur:
            num2 += 1
            cur = cur.next

        cur = l1
        while cur :
            num1 += 1
            cur = cur.next
        #将长的一个链表放在前面
        if num2 > num1:
            l1,l2,num1,num2  = l2,l1,num2,num1

        if add(num1,num2,l1,l2):
            l2 = ListNode(1)
            l2.next = l1
            l1 = l2

        return l1 
        
# @lc code=end

