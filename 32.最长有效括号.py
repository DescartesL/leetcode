#
# @lc app=leetcode.cn id=32 lang=python
#
# [32] 最长有效括号
#

# @lc code=start
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 状态，dp[i]表示从开始到第i个位置的有效括号的个数
        # 状态转移方程 dp[i] = dp[i-1] + 1 or dp[i-1]
        
        
        if not s:
            return 0
        # 创建dp数组
        dp = [0 for _ in range(len(s))]
        
        for i in range(1,len(s)):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[i] = dp[i-2] + 2
                if s[i-1] != "(" and i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1]=="(":
                    dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
        
        return max(dp)
                
# @lc code=end

