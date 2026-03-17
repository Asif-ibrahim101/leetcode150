# Given an m x n 2D binary grid which represents a map of 1 (land) and 0 (water), 
# return the number of islands.
#  An island is surrounded by water and is formed by connecting adjacent land cells horizontally or vertically.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def Valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[m][n] == "1"
        
        def dfs(row, col):
            for dx, dy in direction:
                next_row, next_col = row + dy, col + dx

                if Valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row,  next_col))
                    dfs(next_row, next_col)
        
        direction = [(0,1), (1, 0), (0, -1), (-1, 0)]
        seen = set()
        ans = 0

        m = len(grid)
        n = len(grid[0])

        for row in range(m):
            for col in range(n):
                if grid[m][n] == "1" and (row, col) not in seen:
                    ans += 1
                    seen.add((row, col))
                    dfs(row, col)
        
        return ans
        

