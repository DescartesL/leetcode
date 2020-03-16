#
# @lc app=leetcode.cn id=92 lang=python
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        #找到start的前一个元素prev
        for i in range(m-1): 
            prev = prev.next

        #存储m到n之间的节点
        result = None
        current = prev.next
        for i in range(n-m+1):
            temp = current.next
            current.next = result
            result = current
            current = temp

        prev.next.next = current #current移动到了n+1的位置  prev.next还是保存的是最开始m的元素
        prev.next = result #连接前面
        return dummy.next


        
# @lc code=end

