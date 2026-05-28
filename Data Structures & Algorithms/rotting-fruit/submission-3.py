class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])
        queue = collections.deque()
        visited = set()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        res = 0
        while fresh > 0 and queue:
            new_rotten = False
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in DIRECTIONS:
                    if (x+dx < ROWS and y+dy < COLS and x+dx >= 0 and y+dy >= 0 and 
                                    grid[x+dx][y+dy] == 1 and (x+dx, y+dy) not in visited):
                        new_rotten = True
                        fresh -= 1
                        visited.add((x+dx, y+dy))
                        queue.append((x+dx, y+dy))
            if new_rotten:
                res += 1
        
        if fresh > 0:
            return -1
        else:
            return res