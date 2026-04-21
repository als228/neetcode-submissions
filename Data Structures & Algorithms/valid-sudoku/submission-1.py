class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [[] for _ in range(len(board))]
        squares = [[] for _ in range(len(board))]
        
        for r, row in enumerate(board):
            if not self.isValidSet(row):
                return False
            for c, num in enumerate(row):
                cols[c].append(num)
                squares[r//3 + c//3 * 3].append(num)
        
        for col in cols:
            if not self.isValidSet(col):
                return False

        for square in squares:
            if not self.isValidSet(square):
                return False
        
        return True
            
    def isValidSet(self, coll: List[str]) -> bool:
        nums = set()
        for num in coll:
            if num in nums:
                return False
            elif num.isnumeric():
                nums.add(num)
        return True