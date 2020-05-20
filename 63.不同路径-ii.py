#
# @lc app=leetcode.cn id=63 lang=python
#
# [63] 不同路径 II
#

# @lc code=start
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # dp[i][j]表示有多少条不同的路径
        # 如果遇到障碍，dp[i][j] = 0
        if obstacleGrid[0][0] == 1:
            return 0
        
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        
        # 创建空的dp数组
        dp = [[0]*n for _ in range(m)]
        
        #初始化dp数组
        dp[0][0] = 1
        
        # 处理行
        for i in range(1,m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
            else:
                dp[i][0] = 0
        
        # 处理列
        for j in range(1,n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j-1]
            else:
                dp[0][j] = 0
        
        
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0
                
        return dp[-1][-1]
                    
# @lc code=end

