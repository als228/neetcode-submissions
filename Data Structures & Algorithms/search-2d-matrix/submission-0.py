class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lRow, rRow = 0, len(matrix)-1
        lCol, rCol = 0, len(matrix[0])-1

        while (rRow >= lRow):
            midRow = lRow + (rRow-lRow)//2
            if (matrix[midRow][lCol] > target):
                rRow = midRow-1
            elif (matrix[midRow][rCol] < target):
                lRow = midRow+1
            else:
                while (rCol >= lCol):
                    midCol = lCol + (rCol - lCol)//2
                    if (matrix[midRow][midCol] < target):
                        lCol = midCol+1
                    elif (matrix[midRow][midCol] > target):
                        rCol = midCol-1
                    else:
                        return True
        
        return False