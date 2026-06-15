class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]
        safe = set()

        def bfs(x, y):
            q = deque([(x, y)])
            while q:
                r, c = q.popleft()
                safe.add((r, c))
                for dr, dc in DIRECTIONS:
                    nr, nc = r+dr, c+dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == "O" and (nr, nc) not in safe):
                        q.append((nr, nc))
        
        for r in range(ROWS):
            if board[r][0] == "O" and (r, 0) not in safe: 
                bfs(r, 0)
            if board[r][COLS-1] == "O" and (r, COLS-1) not in safe: 
                bfs(r, COLS-1)
        
        for c in range(COLS):
            if board[0][c] == "O" and (0, c) not in safe: 
                bfs(0, c)
            if board[ROWS-1][c] == "O" and (ROWS-1, c) not in safe: 
                bfs(ROWS-1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in safe:
                    board[r][c] = "X"