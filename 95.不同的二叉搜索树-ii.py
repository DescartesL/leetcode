#
# @lc app=leetcode.cn id=95 lang=python
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generate_trees(start,end):
            if start > end:return [None,] 

            result = []
            for i in range(start,end+1):
                left_tree = generate_trees(start,i-1)
                right_tree = generate_trees(i+1,end)
                
                for l in left_tree:
                    for r in right_tree:
                        current = TreeNode(i)
                        current.left = l
                        current.right = r
                        result.append(current)
            return result
        return generate_trees(1,n) if n else []  
             
            
# @lc code=end

