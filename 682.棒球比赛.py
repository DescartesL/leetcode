#
# @lc app=leetcode.cn id=682 lang=python
#
# [682] 棒球比赛
#

# @lc code=start
class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for op in ops:
            if op == "+":
                num1 = stack[-1]
                num2 = stack[-2]
                result = num1 + num2
                stack.append(result)
            elif op == "C":
                stack.pop()
            elif op == "D":
                temp = stack[-1]
                result = 2 * temp
                stack.append(result)
            else:
                stack.append(int(op))
        return sum(stack)
            
# @lc code=end

