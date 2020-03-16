#
# @lc app=leetcode.cn id=224 lang=python
#
# [224] 基本计算器
#

# @lc code=start
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def caculate(oparetor,num1,num2):
            if oparetor == "+":
                return num2 + num1
            else:
                return num2 - num1
        #进行对应的操作
        def num_and_operator(operator_stack,num_stack):  
            operator =  operator_stack.pop()
            num1 = num_stack.pop()
            num2 = num_stack.pop()
            result = caculate(operator,num1,num2)
            num_stack.append(result)
        #定义优先级
        rank = {"+":1,"-":1,"(":100,")":-100}
        
        num_stack = []
        operator_stack = []
        #enumerate()方法：
        #enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
        #其中数据下标在前，数据在后
        #ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。
        #也就是返回一个对应字符的ASCII码
        for i,c in enumerate(s):
            #处理空格
            if c == " ":
                continue
            #处理数字
            if c >="0" and c <= "9":
                if i != 0 and s[i-1] >="0" and s[i-1]<="9":
                    num_stack[-1] = num_stack[-1] * 10 + ord(c) -ord("0") #ord(c)-ord('0')也就是求c的数值，其实只用int(c)就可以了，这样看起来比较装逼
                else:
                    num_stack.append(int(c))
            #一般操作符
            elif c == "+" or c == "-":
                while (len(operator_stack) != 0) and (rank[c] >= rank[operator_stack[-1]]):
                    num_and_operator(operator_stack,num_stack)
                operator_stack.append(c)
            #操作符是括号
            elif c == "(":
                operator_stack.append(c)
            elif c == ")":
                while operator_stack[-1] != "(":
                    num_and_operator(operator_stack,num_stack)
                operator_stack.pop()
        while len(operator_stack) != 0:
            num_and_operator(operator_stack,num_stack)
        return num_stack[0]



         
                
            
# @lc code=end

