#
# @lc app=leetcode.cn id=15 lang=python
#
# [15] 三数之和
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 特判
        if not nums or len(nums) < 3:
            return []
        # 排序
        nums = sorted(nums)
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                return result
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums)-1
            while left<right:
                res =nums[i] + nums[left] + nums[right]
                if res < 0:
                    left += 1
                elif res > 0:
                    right -= 1
                else:
                    result.append([nums[i],nums[left],nums[right]])
                    while (left<right and nums[left]==nums[left+1]):
                        left += 1
                    while (left<right and nums[right]==nums[right-1]):
                        right -= 1
                    left += 1
                    right -= 1            
        return result                                    
                    
        
# @lc code=end

