#
# @lc app=leetcode.cn id=402 lang=python
#
# [402] 移掉K位数字
#

# @lc code=start
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        #栈的三个步骤，入栈什么？什么时候入栈？什么时候出栈?
        #每个元素先入栈，如果当前元素比栈顶元素大，则舍弃这个元素，k-1
        #如果当前元素比栈顶元素小，则删除栈顶元素，将该元素入栈，如果该元素是0则continue
        stack = []
        for digit in num:
            #如果当前k值为0，那么直接将该元素入栈
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            
            stack.append(digit)
        
        #以下代码可以替换为
        # - Trunk the remaining K digits at the end
        # - in the case k==0: return the entire list
        # finalStack = numStack[:-k] if k else numStack      
        # trip the leading zeros
        # return "".join(finalStack).lstrip('0') or "0"

        while k > 0 and stack:
            stack.pop()
            k -= 1

        if not stack:
            return "0"
        while stack[0] == "0" and len(stack) > 1:
            stack.pop(0)
        res = ''.join(stack)
        
        return res



        
# @lc code=end

