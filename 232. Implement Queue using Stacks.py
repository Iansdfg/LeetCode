class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.queue.insert(len(self.queue), x)
        
        
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.queue.insert(len(self.queue), self.queue[0])
        self.queue.remove(self.queue[0])
        return self.queue.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.queue
