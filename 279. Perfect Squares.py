from collections import deque
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        queue = deque([(0,0)])
        visited = set()
        while queue:
            val, step = queue.popleft()
            step+=1
            for num in range(1,n+1):
                k = val + (num*num)
                if k>n:
                    break
                elif k == n:
                    return step
                if k not in visited:
                    visited.add(k)
                    queue.append((k, step))
                
