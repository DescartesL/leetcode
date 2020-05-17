#
# @lc app=leetcode.cn id=16 lang=python
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums)<3:
            return 0
        
        minnum =  0
        for i in range(len(nums)):
            l = i
            r = len(nums)-1
            while l < r:
                res = nums[i] + nums[l] + nums[r]
                 minnum = min(abs(target-res),minnum)
        
        return minnum
# @lc code=end

