class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        N = len(grid)
        visited = set([(0, 0)])
        q = [[grid[0][0], 0, 0]]

        while q:
            t, x, y = heapq.heappop(q)
            # base case
            if x == N-1 and y == N-1:
                return t
            for dx, dy in DIRECTIONS:
                nx, ny = x+dx, y+dy
                if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited: 
                    visited.add((nx, ny))
                    heapq.heappush(q, [max(t, grid[nx][ny]), nx, ny])