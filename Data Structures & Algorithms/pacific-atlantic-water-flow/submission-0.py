class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]
        dp_pacific = set()
        dp_atlantic = set()

        def dfs(x, y, hashset):
            hashset.add((x, y))
            for dx, dy in DIRECTIONS:
                nx, ny = x+dx, y+dy
                if (0 <= nx < ROWS 
                    and 0 <= ny < COLS 
                    and (nx, ny) not in hashset 
                    and heights[nx][ny] >= heights[x][y]):
                    dfs(nx, ny, hashset)

        # populate two DP tables
        for r in range(ROWS):
            if (r, 0) not in dp_pacific:
                dfs(r, 0, dp_pacific)
            if (r, COLS-1) not in dp_atlantic:
                dfs(r, COLS-1, dp_atlantic)
        for c in range(COLS):
            if (0, c) not in dp_pacific:
                dfs(0, c, dp_pacific)
            if (ROWS-1, c) not in dp_atlantic:
                dfs(ROWS-1, c, dp_atlantic)
        
        return [[r, c] for (r, c) in dp_pacific & dp_atlantic]