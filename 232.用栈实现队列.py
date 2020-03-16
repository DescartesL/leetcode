#
# @lc app=leetcode.cn id=232 lang=python
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._stack1 = []
        self._stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self._stack1.append(x)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if  len(self._stack2) == 0 :
            while len(self._stack1) != 0:
                self._stack2.append(self._stack1.pop())
            
        return self._stack2.pop()


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self._stack2:
            return self._stack2[-1]
        elif not self._stack2 and self._stack1:
            return self._stack1[0]
        else:
            return None


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self._stack1 == [] and self._stack2 == []



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

