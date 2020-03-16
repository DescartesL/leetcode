#
# @lc app=leetcode.cn id=7 lang=python
#
# [7] 整数反转
#

# @lc code=start
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp = abs(x)
        y = 0
        i = len(str(temp))

        while i>0:
            y = y * 10 + temp % 10
            temp //= 10
            i -= 1
        
        if x < 0:
            y = -y
        
        if y < -(2**31) or y > (2**31 - 1) :
            return 0
        
        return y
        
# @lc code=end

