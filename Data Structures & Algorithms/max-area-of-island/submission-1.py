class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(x, y):
            if x < 0 or y < 0 or x >= ROWS or y >= COLS or (x,y) in visited or grid[x][y] == 0:
                return 0

            visited.add((x, y))
            return (1 + dfs(x+1, y)
                    + dfs(x, y+1)
                    + dfs(x-1, y)
                    + dfs(x, y-1))
        
        res = 0
        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == 1 and (x,y) not in visited:
                    res = max(res, dfs(x, y))
        
        return res