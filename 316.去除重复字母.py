#
# @lc app=leetcode.cn id=316 lang=python
#
# [316] 去除重复字母
#

# @lc code=start
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        #字典序：字典序就是指从前往后比较两个字符串大小的方法
        stack = ['0']
        for i,c in enumerate(s):
            if c not in stack:
                while c < stack[-1] and stack[-1] in s[i+1:]:
                    stack.pop()
                stack.append(c)
        
        return ''.join(stack[1:])
                


# @lc code=end

