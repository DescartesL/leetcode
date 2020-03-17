#
# @lc app=leetcode.cn id=503 lang=python
#
# [503] 下一个更大元素 II
#

# @lc code=start
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #通过两次循环遍历数组实现
        #还是通过栈不过这个只需要两个栈就可以了
        #这道题因为可能存在相同的元素值，所以选择在hashtable中存储对应元素的index
        stack = []
        result = {}
        for i in range(len(nums)):
            if not stack:
                stack.append(i)
                continue
            if nums[i] < nums[stack[-1]]:
                stack.append(i)
            else:
                while stack and nums[i] > nums[stack[-1]]:
                    temp = stack.pop()
                    result[temp] = nums[i]
                stack.append(i)

        #此时栈中没有找到对应元素的元素需要进行二次遍历
        for i in range(len(nums)):
            while stack and  nums[i] >nums[stack[-1]]:
                temp = stack.pop()
                result[temp] = nums[i]
        while stack:
            temp = stack.pop()
            result[temp] = -1
        
        res = []
        for i in sorted(result):
            res.append(result[i])
        return res


# @lc code=end

