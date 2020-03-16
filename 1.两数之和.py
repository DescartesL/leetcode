#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index,num in enumerate(nums):#enumertate()函数用于将一个可遍历的数据对象组合成为一个索引序列，同时列出数据和数据下标
            hashmap[num] = index
        for i,num in enumerate(nums):
            j = hashmap.get(target-num)
            if j is not None and  i != j:
                return [i,j]
# @lc code=end

