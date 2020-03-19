#
# @lc app=leetcode.cn id=636 lang=python
#
# [636] 函数的独占时间
#

# @lc code=start
class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        #使用栈存储一个元组或者list，第一个元素保存函数，一个元素保存运行时间
        #当遇到start时直接将函数和运行时间入栈
        #当遇到end时将栈顶元素拿出来重新计算时间 current - temp +1
        #如果此时栈内还有元素，那么就要更新此时的栈顶元素时间
        stack = []
        time = [0 for i in range(n)]
        for log in logs:
            current = log.split(":")
            if current[1] == "start":
                stack.append([int(current[0]),int(current[2])])
            else:
                progress = int(current[0])
                temp = stack.pop()
                now = int(current[2])- temp[1] + 1
                if len(stack) != 0:
                    time[stack[-1][0]] -= now
                time[progress] += now
        return time 
        
        
                




        
# @lc code=end

