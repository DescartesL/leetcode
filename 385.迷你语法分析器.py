#
# @lc app=leetcode.cn id=385 lang=python
#
# [385] 迷你语法分析器
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        if s[0]!= "[":
            return NestedInteger(int(s))
        #栈用于保存NestedInteger对象
        #栈的三个问题：入栈什么？什么时候入栈？什么时候出栈？
        #入栈NestedInteger对象
        #遇到左括号时入栈一个空的对象
        #如果遇到左括号或者是逗号，就出栈，充满对象以后在入栈
        stack = []
        #num用于保存当前数字，sign表示正负，is_num用于保存前一个数字是否还是数字
        num ,sign,is_num = 0,1,False
        for c in s:
            #如果是数字的话，由于是字符串，字符串中的数字处理方式则需要考虑几个方面，1，数字的位数；2，数字的正负，因此要在前面maintain几个变量
            if c.isdigit():
                num = num * 10 + int(c)
                is_num = True
            elif c == "-":
                sign = -1
            #如果遇到[，那么就入栈一个空的NestedInteger对象
            elif c == "[" :
                stack.append(NestedInteger())
            #如果遇到]或者逗号，那么把栈顶的对象元素拿出来,将数组元素入栈
            elif c == "]" or c == ",":
                if is_num:
                    current= stack.pop()
                    current.add(NestedInteger(num * sign))
                    stack.append(current)
                #遇到]和,以后，说明一个元素已经结束了，那么将原数字状态重置
                num ,sign,is_num = 0,1,False
                
                #此时是嵌套列表
                if c == "]" and len(stack) > 1:
                    current = stack.pop()
                    stack[-1].add(current)
        
        return stack[0]
                








        
# @lc code=end

