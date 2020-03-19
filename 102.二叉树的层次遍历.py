#
# @lc app=leetcode.cn id=102 lang=python
#
# [102] 二叉树的层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # from collections import deque
        # result = []
        # if not root:return result
        # level = 0
        # queue = deque([root,])
        # while queue:
        #     result.append([])
        #     level_length = len(queue)
        #     for i in range(level_length):
        #         node = queue.popleft()
        #         result[level].append(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
            
        #     level += 1
        # return result
        if not root :
            return []
        res = []
        queue = [root]
        while queue:
            size = len(queue)
            temp = []
            for i in xrange(size):
                r = queue.pop(0)
                temp.append(r.val)
                if r.left:
                    queue.append(r.left)
                if r.right:
                    queue.append(r.right)
            res.append(temp)
        return res


# @lc code=end

