class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # setup
        q = collections.deque()
        DIRECTIONS = [(1, 0), (0, 1), (-1,0), (0,-1)]
        ROWS, COLS = len(grid), len(grid[0])

        # get coordinates of all 0s
        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == 0:
                    q.append((x, y))

        # go thru all 0s and close neighbors
        while q:
            x, y = q.popleft()
            for dx, dy in DIRECTIONS:
                nx, ny = x+dx, y+dy
                if (0 <= nx < ROWS and 0 <= ny < COLS and grid[nx][ny] != -1 and grid[nx][ny] > grid[x][y]+1):
                    grid[nx][ny] = 1+grid[x][y]
                    q.append((nx, ny))