#
# @lc app=leetcode.cn id=71 lang=python
#
# [71] 简化路径
#

# @lc code=start
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        #思路，使用栈存储两个斜杠之间的内容
        stack = []
        path2 = path.split("/")
        for i in path2:
            if i == "" or i == ".":
                continue
            elif i =="..":
                if len(stack) != 0:
                    stack.pop()
            else:
                stack.append(i)

        result = []
        #如果给定的参数是空的，那就只返回一个"/"
        if len(stack) == 0:
            return "/"
        result = ["/" + i for i in stack]
        result "".join(result)

# @lc code=end

