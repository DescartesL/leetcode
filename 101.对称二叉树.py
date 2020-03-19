#
# @lc app=leetcode.cn id=101 lang=python
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #递归的一个重要的要素，Base
        if not root:return True
        def __isSymmetric(nodeA,nodeB):
            if not nodeA and not nodeB:
                return True
            if not nodeA or not nodeB:
                return False
            if nodeA.val != nodeB.val:
                return False
            return  __isSymmetric(nodeA.left,nodeB.right) and __isSymmetric(nodeA.right,nodeB.left)
        
        return __isSymmetric(root.left,root.right)

# @lc code=end

