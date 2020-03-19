#
# @lc app=leetcode.cn id=98 lang=python
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def __isValidBST(self,root,minval = float('-inf'),maxval = float('inf')):
    #     if not root:return True
    #     if root.val <= minval or root.val >= maxval:return False
    #     return self.__isValidBST(root.left,minval,root.val) and self.__isValidBST(root.right,root.val,maxval)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #递归的解法
        # return self.__isValidBST(root)
        #迭代的解法：
        # stack = [(root,float('-inf'),float('inf'))]
        # while stack:
        #     node,minval,maxval = stack.pop()
        #     if not node :continue
        #     val = node.val
        #     if val <= minval or val >=maxval:return False
        #     stack.append((node.left,minval,val))
        #     stack.append((node.right,val,maxval))
        # return True
        #中序遍历的方法：很明显，BST中序遍历是个递增的列表
        stack,inorder = [],float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True


    
        
# @lc code=end

