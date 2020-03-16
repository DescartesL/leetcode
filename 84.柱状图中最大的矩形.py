#
# @lc app=leetcode.cn id=84 lang=python
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        #这里栈里存储的是各元素的下标，思路就是找到i元素的左边第一个小于和右边第一个大于的元素，此时最大面积则由这两个决定
        stack = []
        #减少边界条件的判断
        heights.append(0)

        max_Area = 0
        #如果当前元素比栈顶元素大则入栈，如果当前元素比栈顶元素小则出栈
        for i in range(len(heights)):
            #如果栈为空，则直接将下标入栈
            while stack and heights[stack[-1]] >= heights[i]:
                last = stack.pop()
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                max_Area = max(max_Area , heights[last] * width)
            stack.append(i)
        return max_Area

# @lc code=end

