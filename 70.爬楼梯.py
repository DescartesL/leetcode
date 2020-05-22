#
# @lc app=leetcode.cn id=70 lang=python
#
# [70] 爬楼梯
#

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 状态: dp[i]代表到第i层有多少种不同的
        # 状态转移方程：dp[i] = dp[i-1] + dp[i-2]
        if n < 2:
            return n
        
        # 创建dp数组
        dp = [0 for _ in range(n+1)]
        
        # 初始化dp数组
        dp[1], dp[2] = 1, 2
        
        # 填满dp数组
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2] 
        
        return dp[-1]
            
# @lc code=end

