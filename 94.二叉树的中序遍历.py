#
# @lc app=leetcode.cn id=94 lang=python
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #方法一：栈
        # stack = []
        # result = []
        # point = root
        # while stack or point:
        #     if point:
        #         stack.append(point)
        #         point = point.left
        #     else:
        #         temp = stack.pop()
        #         result.append(temp.val)
        #         point = temp.right
        # return result   
        #方法二：递归
        # result = []
        # def dfs(root):
        #     if  not root:
        #         return 
        #     dfs(root.left)
        #     result.append(root.val)
        #     dfs(root.right)
        
        # dfs(root)
        # return result
        stack = []
        result = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                temp = stack.pop()
                result.append(temp.val)
                root = temp.right
        return result

                


            
            

# @lc code=end

