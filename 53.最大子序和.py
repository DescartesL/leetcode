#
# @lc app=leetcode.cn id=53 lang=python
#
# [53] 最大子序和
#

# @lc code=start
class Solution(object):
    def cross_nums(self,nums,left,right,mid):
        if left == right:
            return nums[left]
        
        #左边部分
        left_max = float('-inf')
        current_sum = 0
        for i in range(mid,left-1,-1):
            current_sum += nums[i]
            left_max = max(current_sum,left_max)
        
        #右边部分
        right_max = float('-inf')
        current_sum = 0
        for i in range(mid + 1,right + 1):
            current_sum += nums[i]
            right_max = max(current_sum,right_max)
        
        return left_max + right_max 


    def helper(self,nums,left,right):
        #只有一个元素时
        if left == right:
            return nums[left]
        
        mid = (left + right) // 2
        left_sums = self.helper(nums,left,mid)
        right_sums = self.helper(nums,mid + 1,right)
        cross_sums = self.cross_nums(nums,left,right,mid)

        return max(left_sums,right_sums,cross_sums) 

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.helper(nums,0,len(nums)-1)
    


# @lc code=end

