#
# @lc app=leetcode.cn id=64 lang=python
#
# [64] 最小路径和
#

# @lc code=start
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # dp[i][j]指到达i,j位置的最短路径和
        # 状态转移方程dp[i][j] = min(dp[i][j-1]+grid[i][j], dp[i-1][j]+grid[i][j])
        # 如果处于边界上，那么之和当前元素和前一个元素的和有关
        m, n =len(grid),len(grid[0]) 
        dp = [[0]*n for _ in range(m)]
        
        # 初始化dp数组
        dp[0][0] = grid[0][0]
        
        # 初始化行
        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        # 初始化列
        for j in range(1,n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        # 填满整个dp数组
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i-1][j] + grid[i][j] , dp[i][j-1] + grid[i][j]  )
                
        return dp[-1][-1]
# @lc code=end

