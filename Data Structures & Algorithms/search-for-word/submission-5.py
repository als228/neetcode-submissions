class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(index, r, c):
            # word found
            if index == len(word):
                return True
            # base case
            if (0 > r or r == ROWS 
                or 0 > c or c == COLS 
                or (r, c) in visited 
                or board[r][c] != word[index]):
                return False

            visited.add((r, c))
            found = (dfs(index+1, r+1, c) or 
                    dfs(index+1, r, c+1) or
                    dfs(index+1, r-1, c) or
                    dfs(index+1, r, c-1)
            )
            visited.remove((r, c))
            return found
        
        # do dfs if 1st letter found
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(0, r, c):
                        return True
        # if 1st letter not found
        return False