#
# @lc app=leetcode.cn id=150 lang=python
#
# [150] 逆波兰表达式求值
#

# @lc code=start
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        num_stack = []
        for i in tokens:
            if i != "+" and i !="-" and i != "*" and i != "/":
                num_stack.append(int(i))
            elif i == "+":
                num1 = num_stack.pop()
                num2 = num_stack.pop()
                result = num2 + num1
                num_stack.append(result)
            elif i == "-":
                num1 = num_stack.pop()
                num2 = num_stack.pop()
                result = num2 - num1
                num_stack.append(result)
            elif i == "*":
                num1 = num_stack.pop()
                num2 = num_stack.pop()
                result = num2 * num1
                num_stack.append(result)
            elif i == "/":
                num1 = num_stack.pop()
                num2 = num_stack.pop()
                if num2 * num1 >= 0:
                    result = num2 // num1
                else:
                    result = -(-num2 // num1)
                num_stack.append(result)
        res = num_stack.pop()
        return int(res)

# @lc code=end

