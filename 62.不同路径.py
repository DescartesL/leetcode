#
# @lc app=leetcode.cn id=62 lang=python
#
# [62] 不同路径
#

# @lc code=start
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # 而在边界上的话都只有一种走路方法
        dp = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]
                    
# @lc code=end

