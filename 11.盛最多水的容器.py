#
# @lc app=leetcode.cn id=11 lang=python
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height)-1
        maxwater = 0
        while left<right:
            maxwater = max(maxwater ,min(height[left],height[right]) * (right-left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return maxwater
# @lc code=end

