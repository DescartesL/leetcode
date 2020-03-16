#
# @lc app=leetcode.cn id=9 lang=python
#
# [9] 回文数
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # n = str(x)
        # a = list(n)
        # a.reverse()
        # if a[0] == "-":return False
        # elif a == list(str(x)):
        #     return True
        # else:
        #     return False
        return True if str(x)==str(x)[::-1] else False
# @lc code=end

