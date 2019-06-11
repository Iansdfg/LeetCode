class MyStack1(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.stack.insert(0,x)
        for i in range(len(self.stack)-1):
            self.stack.insert(0,self.stack[-1])
            self.stack.pop()

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.stack.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.stack[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if not self.stack:
            return True
        else:
            return False

class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []
        self.topp = None

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.queue1.insert(0,x)
        self.topp = x

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        while len(self.queue1) > 1:
            self.topp = self.queue1.pop()
            self.queue2.insert(0, self.topp)
        res = self.queue1.pop()
        self.queue1,self.queue2 = self.queue2,self.queue1
        return res

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.topp


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if not self.queue1: return False
        else:return True

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(1)
# obj.push(2)
# obj.push(3)
# obj.push(4)
# param_2 = obj.pop()
# print(param_2)
# param_3 = obj.top()
# param_4 = obj.empty()
