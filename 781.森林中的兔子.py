#
# @lc app=leetcode.cn id=781 lang=python
#
# [781] 森林中的兔子
#

# @lc code=start
class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        #思路：既然要求有最少的兔子，那么肯定回答相同数字的兔子就是相同的颜色，那么这个颜色的兔子就是1+answer个，那么有不同答案的兔子就是不同颜色的兔子
        #使用一个数组来存储兔子的个数，只用来存储不同颜色的兔子个数，最后返回这个数组的sum就可以了
        #选择使用hashtable来解题
        if len(answers) == 0:
            return 0 
        result = {} #hash表存储说answer的兔子的只数
        for i in answers:
            if i in result:
                result[i] +=  1
            else:
                result[i] = 1
        count = 0
        for i in result.keys():
            count += (result[i]//(i+1))*(i+1)
            if result[i] % (i+1)!=0:
                count += i+1
        return count
        
        

# @lc code=end

