#
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if  not s :
            return True
        stack = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            
            elif i ==")":
                if not stack  or stack.pop() !="(":
                    return False

            elif i == "}":
                if not stack or stack.pop() != "{":
                    return False
            else:
                if not stack or stack.pop() != "[":
                    return False
        if stack:
            return False
        
        return True
                
# @lc code=end

