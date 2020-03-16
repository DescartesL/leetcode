#
# @lc app=leetcode.cn id=141 lang=python
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #使用双指针    
        slow,fast = head,head
        while slow and fast:
            slow = slow.next

            #这里的边界条件十分重要，必须要满足fast可以跳两次，不然就是False，因为如果有环是不可能不能跳两次的
            #fast一次跳两步，所以要判断fast和fast.next是否存在，否则要报错NoneType
            if fast.next:
                fast = fast.next.next
            else:
                return False

            if fast == slow :
                return True
            else:
                continue
        return False
        
# @lc code=end

