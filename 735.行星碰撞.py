#
# @lc app=leetcode.cn id=735 lang=python
#
# [735] 行星碰撞
#

# @lc code=start
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        #入栈什么？什么时候入栈？什么时候出栈？
        #遇到正数，直接入栈
        #遇到负数，循环判断栈顶元素是不是正数，如果是正数则判断两者加和是否大于0，大于零负数滚，小于零正数滚，等于零两个都滚
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                #负数大
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                #相等
                elif stack[-1] == -asteroid:
                    stack.pop()
                #负数小
                break
            else:
                stack.append(asteroid)

        return stack
         
# @lc code=end

