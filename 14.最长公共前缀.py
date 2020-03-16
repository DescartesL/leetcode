#
# @lc app=leetcode.cn id=14 lang=python
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs != []:

            strs_matrix = []
            for element in strs:
                strs_matrix.append(list(element))

            prefix = []
            temp = []
            end = 0
            for j in range(len(strs_matrix[0])):

                for i in range(len(strs_matrix)):

                    if len(strs_matrix[i]) == len(prefix):
                        end = 1
                        break
                    
                    temp.append(strs_matrix[i][j])
                    
                if end == 1:
                    break

                if len(set(temp)) == 1:
                    prefix.extend(list(set(temp)))
                    temp = []
                else:
                    break

            if prefix == []:
                return ""

            return ''.join(prefix)

        else:
            return ""

# @lc code=end

