#
# @lc app=leetcode.cn id=42 lang=python
#
# [42] 接雨水
#

# @lc code=start
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #思路：每根柱子的高度的方向可以接水的数量：min(当前柱子往左的最高值，当前柱子往右的最高值)-当前柱子的高度
        #再用一个全局变量存储每根柱子的相应的接水的数量
        left, right = [0]*len(height),[0]*len(height)#保存从左到右从右到左当前下标的最高柱子高度
        left_max,right_max,count = -1,-1,0
        for i in range(len(height)):
            if height[i] > left_max:
                left_max = height[i]
            left[i] = left_max
            if height[len(height)-1-i] > right_max:
                right_max = height[len(height)-1-i]
            right[len(height)-1-i] = right_max

        #遍历数组，只有当前柱子的左最高 和右最高都比当前元素大时才能接到雨水
        for i in range(len(height)):
            if height[i] < left[i] and height[i] < right[i]:
                count += min(left[i],right[i]) - height[i]
        
        return count
            
        
# @lc code=end

