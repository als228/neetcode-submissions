class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[-1, 0], [0, -1], [1, 0], [0,1]]
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        def dfs(row, col):
            if (row < 0 or col < 0 or row >= ROWS or col >= COLS or ((row, col) in visited) or grid[row][col] == "0"):
                return
            visited.add((row, col))

            for rd, cd in directions:
                dfs(row+rd, col+cd)
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    islands += 1
        
        return islands