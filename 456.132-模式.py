#
# @lc app=leetcode.cn id=456 lang=python
#
# [456] 132模式
#

# @lc code=start
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #栈的三要素：存什么？什么时候出栈？什么时候入栈？
        # stack = []
        # for i in range(len(nums)):
        #     #栈为空的时候直接入栈
        #     if not stack:
        #         stack.append(nums[i])
        #         continue
        #     #栈中只有一个元素的情况，比较当前元素是否小于栈顶元素，如果小于，那么就栈顶元素出栈，将当前元素入栈
        #     elif len(stack)==1:
        #         if nums[i] < stack[-1]:
        #             stack.pop()
        #             stack.append(nums[i])
        #         else:
        #             stack.append(nums[i])
        #     #栈中有两个元素的情况，如果当前元素小于栈顶元素，则直接入栈，否则有两种情况，要么把较大元素入栈，或者是不入栈，不过要是有132的情况，后面元素肯定有比这个更大的元素更小的值，所以选择将较大的元素入栈
        #     elif len(stack) == 2 :
        #         if nums[i] >= stack[-1]:
        #             stack.pop()
        #             stack.append(nums[i])
        #         elif nums[i] > stack[0]:
        #             stack.append(nums[i])
        #     #栈中有三个元素的情况
        #     elif len(stack) == 3:
        #         return True
        # if len(stack) == 3:
        #     return  True
        # return False
        #以上是错误解法
        #维护一个从尾到头的递增栈，max保存栈中最大元素,其实就是栈顶元素，mid保存中间元素，如果能找到一个满足小于mid的元素，那么就一定满足ai<ak<aj,那么就可以得出结论
        stack = []
        _mid = float("-inf")
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < _mid:
                return True
            while stack and nums[i]> stack[-1]:
                _mid = stack.pop()
            stack.append(nums[i])
        return False
        
# @lc code=end

