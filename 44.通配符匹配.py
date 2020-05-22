#
# @lc app=leetcode.cn id=44 lang=python
#
# [44] 通配符匹配
#

# @lc code=start
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # dp[i][j]代表s的前i个元素和p的前j个元素是否匹配
        # 如果s[i] == p[j]: dp[i][j] = dp[i-1][j-1]
        # 如果p[j] == "?": dp[i][j] = dp[i-1][j-1]
        # 如果p[j] == "*":
        # 1，p[j+1]存在 
        #       1,s[i] == p[j+1]   * 表示空时，dp[i][j] = dp[i][j-1]
        #       2,s[i] != p[j+1]  *表示字符串时，但是后面还有新的字符 
        # 2，p[i+1]不存在
        #       dp[i][j] 从当前到最后都是True
        
        s = '0'+s
        p = '0'+p
        
        s_len, p_len = len(s), len(p)
        
        dp = [[False]*p_len for _ in range(s_len)]
                
        # 初始化
        dp[0][0] = True
        for j in range(1,p_len):
            if p[j] == '*':
                dp[0][j] = dp[0][j-1]
        for i in range(1,s_len):
            dp[i][0] = False
        
        for i in range(1,s_len):
            for j in range(1,p_len):
                if s[i] == p[j] or p[j] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] == '*' :
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return dp[-1][-1]
                    
        
        
# @lc code=end

