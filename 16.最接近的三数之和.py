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
        if not nums or len(nums) < 3:
            return 0
        nums = sorted(nums)
        result = float("inf")
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                res = nums[i] + nums[left] + nums[right]
                if abs(result - target) > abs(res - target):
                    result = res 
                if res < target:
                    left += 1
                elif res > target:
                    right -= 1
                else:
                    return target
        return result
# @lc code=end

