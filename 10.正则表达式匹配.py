#
# @lc app=leetcode.cn id=10 lang=python
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # 为了保证s[i]是第i个字符，p[j]是第j个字符
        s = " "+s
        p = " "+p        
        # dp[i][j] 表示从s[i]之前的部分能否被p[j]之前的部分匹配到
        # 状态转移方程 dp[i][j] = dp[i-1][j-1] and ( p[j] == '.' or s[i] == p[j] )
        s_len, p_len = len(s), len(p)
        # 创建dp数组
        dp = [[False for _ in range(p_len)] for _ in range(s_len)]
        
        # 初始化
        dp[0][0] = True
        
        for i in range(2,p_len):
            dp[0][i] = dp[0][i-2] and p[i] == '*'
                
        for i in range(1,s_len):
            for j in range(1,p_len):
                if p[j] == s[i] or p[j] =='.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] == '*':
                    if p[j-1] != s[i]:
                        dp[i][j] = dp[i][j-2]
                    if p[j-1] == s[i] or p[j-1] == '.':
                        dp[i][j] = dp[i-1][j] or dp[i][j-1] or dp[i][j-2]  
                
        
        return dp[-1][-1]
                    
# @lc code=end

