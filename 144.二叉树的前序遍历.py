#
# @lc app=leetcode.cn id=144 lang=python
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #方法一：递归
        # result = []
        
        # def preOrder(root):
        #     if not root:
        #         return
        #     result.append(root.val)
        #     preOrder(root.left)
        #     preOrder(root.right)

        # preOrder(root)
        # return result
        #方法二：栈 
        # if not root:
        #     return []

        # stack = []
        # stack.append(root)
        # result = []
        # while stack :
        #     current = stack.pop()
        #     result.append(current.val)
        #     if current.right:
        #         stack.append(current.right)
        #     if current.left:
        #         stack.append(current.left)
        # return result
        if not root:
            return []
        
        result = []
        stack = []
        stack.append(root)
        while stack:
            temp = stack.pop()
            result.append(temp.val)
            #栈是LIFO，所以先把右子树入栈
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
        return result
# @lc code=end

