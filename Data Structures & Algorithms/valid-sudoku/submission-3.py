class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        col_nums = defaultdict(set)
        quad_nums = defaultdict(set)

        for r in range(ROWS):
            row_nums = set()
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                if board[r][c] in row_nums or board[r][c] in col_nums[c] or board[r][c] in quad_nums[(r // 3, c // 3)]:
                    print(f"Error found at {r} row and {c} col")
                    return False
                row_nums.add(board[r][c])
                col_nums[c].add((board[r][c]))
                quad_nums[(r // 3, c // 3)].add(board[r][c])
        
        return True