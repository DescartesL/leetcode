#
# @lc app=leetcode.cn id=96 lang=python
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 1
        for i in range(0,n):
            c = c * 2*(2*i+1)/(i+2)
        return int(c)
# @lc code=end

