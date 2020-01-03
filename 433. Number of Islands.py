from collections import deque
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        if grid == [] or grid == [[]]:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        cnt = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    visited.add((row, col))
                    self.bfs(grid, row, col, visited)
                    cnt += 1
        return cnt
        
        
    def bfs(self, grid, row, col, visited):
        queue = deque([(row, col)])
        while queue:
            curr_x, curr_y = queue.popleft()
            for delta_x, delta_y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_x, next_y = curr_x + delta_x, curr_y + delta_y
                if self.is_valid(grid, next_x, next_y):
                    grid[next_x][next_y] = 0
                    visited.add((next_x, next_y))
                    queue.append((next_x, next_y))
                    
    def is_valid(self, grid, x, y):
        rows, cols = len(grid), len(grid[0])
        return 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1
            
        
                    
            
        
        
        
    
