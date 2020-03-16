#
# @lc app=leetcode.cn id=145 lang=python
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #方法一：递归
        result = []
        
        def postOrder(root):
            if not root:
                return
            postOrder(root.left)
            postOrder(root.right)
            result.append(root.val)
        
        postOrder(root)
        
        return result
# @lc code=end

