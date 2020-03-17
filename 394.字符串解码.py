#
# @lc app=leetcode.cn id=394 lang=python
#
# [394] 字符串解码
#

# @lc code=start
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        #看到很多括号，就要反应过来使用栈来保存
        #然后思考三个问题：入栈什么元素？什么时候入栈？什么时候出栈？
        #遇到数字直接入栈，遇到字符则判断下一个是不是字符，如果是字符则连接在一起，直到遇到一个数字或者右括号时入栈
        # 遇到右括号时，将字符串出栈，再次将[出栈，遇到数字时把字符串重复，判断栈是否为空，如果为空那么直接将字符串入栈，如果还有字符，就将栈顶元素出栈，再将两个元素连接在一起在入栈
        #maintain一个栈用来保存元素
        # if s == "":
        #     return s 
        # stack = []
        # for i in s:
        #     #如果遇到数字，那么直接入栈
        #     if i.isdigit():
        #         if len(stack) != 0 and type(stack[-1]) == int:
        #             num = stack.pop()
        #             num = num * 10 + int(i)
        #             stack.append(num) 
        #         else:
        #             stack.append(int(i))
        #     #如果遇到[，那么也直接入栈
        #     elif i == "[":
        #         stack.append(i)
        #     elif i.isalpha():
        #         if len(stack)!=0 and stack[-1].isalpha():
        #             temp = stack.pop()
        #             temp = temp + i
        #             stack.append(temp)
        #         else:
        #             stack.append(i)
        #     elif i == "]":
        #         temp  =  stack.pop()
        #         #将左括号出栈
        #         stack.pop()
        #         num = stack.pop()
        #         temp = num * temp
        #         if len(stack) != 0 and stack[-1].isalpha():
        #             temp2 = stack.pop()
        #             temp = temp2 + temp
        #         stack.append(temp)
        
        # return stack[0]

        #栈中不一定只存一个元素，也可以存储一个列表
        stack ,multi,res = [],0,""
        for c in s:
            if c == "[":
                stack.append([multi,res])
                res ,multi= "",0
            elif c == "]":
                cur_mutli,cur_res = stack.pop()
                res = cur_res + cur_mutli * res
            elif c.isdigit():
                multi = multi * 10 + int(c)
            else:
                res += c

        return res
# @lc code=end

