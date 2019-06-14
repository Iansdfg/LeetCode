class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        i = 1
        while i:
            if 2**i == n:
                return True
            if 2**i>n:
                return False
            i+=1
        
