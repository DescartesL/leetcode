#
# @lc app=leetcode.cn id=331 lang=python
#
# [331] 验证二叉树的前序序列化
#

# @lc code=start
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        #思路：每遇到两个#就出栈一个数字，出栈一个数字就加入一个"#"
        #入栈全部元素
        # if preorder == '':
        #     return False
        # if preorder == "#":
        #     return True
        # stack = []
        # preorder_list = preorder.split(",")
        # isLeftTree = True
        # for i in range(len(preorder_list)):
        #     if preorder_list[i].isdigit():
        #         if not isLeftTree:
        #             if not stack:
        #                 return False
        #             stack.pop()
        #         stack.append(preorder_list[i])
        #         isLeftTree = True
        #     else:
        #         isLeftTree = False
        #         if preorder_list[i-1] == "#":
        #             if not stack:
        #                 return False
        #             stack.pop()
                
        # return len(stack) == 0
        slots = 1
        for node in preorder.split(','):
            slots -= 1

            if slots < 0:
                return False
            
            if node != "#":
                slots += 2
            
        return slots == 0



# @lc code=end

