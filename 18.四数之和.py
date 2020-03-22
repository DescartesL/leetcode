#
# @lc app=leetcode.cn id=18 lang=python
#
# [18] 四数之和
#

# @lc code=start
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #双指针,不过双指针解法需要排序，类似快速排序的解法
        #不过这个双指针需要四个指针才能用
        #a,b放在最左边，c是b的下一个，d是最后一个
        #以ab位置为最小值的解需要找另两个较大的值，如果加和大于target d左移，否则c右移，cd相遇时以ab为最小值得组合就求得完毕了，b++进入b循环，b循环结束时进入a循环，都结束时求解完毕
        #O(n3)
        # nums.sort()
        # result = []
        # if len(nums) < 4 : return []
        # for a in range(len(nums)-3):
        #     if a > 0 and nums[a] == nums[a-1]:continue 
        #     for b in range(a+1,len(nums)-2):
        #         if b > a + 1 and nums[b] == nums[b-1]:continue
        #         c = b + 1
        #         d = len(nums)-1
        #         while c < d:
        #             if nums[a] + nums[b] + nums[c] + nums[d] > target:
        #                 d = d - 1
        #             elif nums[a] + nums[b] + nums[c] + nums[d] < target:
        #                 c = c + 1
        #             else:
        #                 result.append(sorted([nums[a],nums[b],nums[c],nums[d]]))
        #                 while c < d and nums[c+1] == nums[c]:
        #                     c = c + 1
        #                 while c < d and nums[d-1] == nums[d]:
        #                     d = d - 1
        #                 c = c + 1
        #                 d = d - 1 
        
        # return result
        nums.sort()
        result = []
        if len(nums) < 4:
            return []
        for a in range(len(nums)-3):
            #判断当前a和前一个a是否时相同得，相同得话就要跳过
            if a > 0 and nums[a] == nums[a-1]:continue
            for b in range(a+1,len(nums)-2):
                #对b进行同样得操作
                if b > a + 1 and nums[b] == nums[b-1]:continue 
                c = b + 1
                d = len(nums)-1
                while c < d:
                    if nums[a] + nums[b] + nums[c] + nums[d] > target:
                        d = d - 1
                    elif nums[a] + nums[b] + nums[c] + nums[d] < target:
                        c = c + 1
                    else:
                        result.append(sorted([nums[a],nums[b],nums[c],nums[d]]))
                        while c < d and nums[c+1] == nums[c]:
                            c = c + 1
                        while c < d and nums[d-1] == nums[d]:
                            d = d - 1
                        c = c + 1
                        d = d - 1
        return result

            
# @lc code=end

