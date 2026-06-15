class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [[1,0], [0,1], [-1,0], [0,-1]]
        visited = set()
        
        def bfs(x, y):
            q = collections.deque([(x,y)])
            visited.add((x, y))
            area = 1

            while q:
                nx, ny = q.popleft()
                for dx, dy in DIRECTIONS:
                    if (0 <= nx+dx < len(grid) 
                        and 0 <= ny+dy < len(grid[0])
                        and (nx+dx, ny+dy) not in visited
                        and grid[nx+dx][ny+dy] == 1):
                        area += 1
                        visited.add((nx+dx, ny+dy))
                        q.append((nx+dx, ny+dy))
            
            return area
        
        res = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 1 and (x, y) not in visited:
                    res = max(res, bfs(x, y))
        
        return res