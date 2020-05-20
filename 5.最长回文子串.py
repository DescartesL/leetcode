#
# @lc app=leetcode.cn id=5 lang=python
#
# [5] 最长回文子串
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 首先判断字符串的长度，如果长度小于2，也就是单字符的字符串
        if len(s)<2:
            return s
        # 创建一个二维的空数组，用来存放dp[i][j],dp[i][j]代表从字符串的i位置到j位置之间的字符串是否是回文串
        dp = [[ False for _ in range(len(s))] for _ in range(len(s))]
        #初始化dp，单个字符也是回文
        for i in range(len(s)):
            dp[i][i] = True
        # 初始化两个变量，分别存储回文的最大字串以及最长回文的起始位置
        max_len, start = 1, 0
        #开始查找
        for j in range(1,len(s)):
            for i in range(0,j):
                # 判断i+1和j-1之间的距离是否小于2，小于2即是一个边界条件,说明当前dp[i][j]已经是回文的了，i,j相等，剩下的字母只有一个，肯定是回文的
                # j-1-(i+1)+1 < 2的情况 ==> j-i<3
                if s[i]==s[j]:
                    if j-i<3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
                
                if dp[i][j]:
                    cur_max_len = j-i+1
                    if cur_max_len>max_len:
                        max_len = cur_max_len
                        start = i
                
        return s[start:start + max_len]
        
# @lc code=end

