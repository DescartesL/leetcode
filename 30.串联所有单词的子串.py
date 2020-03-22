#
# @lc app=leetcode.cn id=30 lang=python
#
# [30] 串联所有单词的子串
#

# @lc code=start
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # #双指针
        # result = []
        # #确定字串长度
        # size = len(words[0])
        # #每size个位置判断一下当前字串是否在words里面。如果不在则后移，如果在就记录当前子串得起始位置
        # #但是可能出现重复得现象，最后要判断结果得长度是否和word长度相同
        # i,j = 0,0
        # current = []
        # while i < len(s):
        #     cur = ''
        #     while j < i + size:
        #         cur = cur + s[j]
        #         j += 1
        #     if cur in words:
        #         current.append(i)
        #         i += size
        #     else:
        #         if len(current) < len(words):
        #             current.clear()
        #         else:
        #             result.append(current[0])
        #             current.clear()
        #             i += size
        
        # return result
        #滑动窗口加哈希表
        if not s or len(s) == 0 or not words or len(words) == 0: return []
        words_map,res = dict(),[]
        #构造哈希表
        for i in words:
            if i not in words_map:
                words_map[i] = 1
            else:
                words_map[i] += 1
        
        one_word_size = len(words[0])
        all_words_size = len(words) * one_word_size

        for i in xrange(len(s)-all_words_size+1):
            #每次取all_words_size长度得子串
            temp_str,d = s[i:i+all_words_size],dict(words_map)
            #将字串和临时字典进行比较
            for j in xrange(0,len(temp_str),one_word_size):
                #从字串temp_str中取出one_word_size长度得字串，看是否存在于临时字典中
                #如果是则将临时字典记录的频率-1，如果不在就跳出循环
                key = temp_str[j:j+one_word_size]
                if key in d:
                    d[key] -= 1
                    if d[key] == 0:del d[key]
                else:
                    break
            if not d:
                res.append(i)
        return res
# @lc code=end

