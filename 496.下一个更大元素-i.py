#
# @lc app=leetcode.cn id=496 lang=python
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #用什么栈？什么入栈？什么时候入栈？什么时候出栈？
        stack = []
        result = {}
        for i in range(len(nums2)):
            if not stack:
                stack.append(nums2[i])
            if nums2[i] < stack[-1]:
                stack.append(nums2[i])
            else:
                while stack and nums2[i] > stack[-1]:
                    temp = stack.pop()
                    result[temp] = nums2[i]
                stack.append(nums2[i])
        while stack:
            temp = stack.pop()
            result[temp] = -1
        
        res = []
        for i in range(len(nums1)):
            res.append(result[nums1[i]])
        
        return res
        
        




        
# @lc code=end

