#
# @lc app=leetcode.cn id=341 lang=python
#
# [341] 扁平化嵌套列表迭代器
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.d = []
        def f(nestedList):
            for nested in nestedList:
                if nested.isInteger():
                    self.d.append(nested.getInteger())
                else:
                    f(nested.getList())
        f(nestedList)
        self.i,self.n = -1,len(self.d) - 1

                
        

    def next(self):
        """
        :rtype: int
        """
        self.i += 1
        return self.d[self.i]
        

        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i < self.n

        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end

