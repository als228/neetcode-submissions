class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1

        while l <= r:
            mid_row = (l+r) // 2
            row = matrix[mid_row]
            if target < row[0]:
                r = mid_row - 1
            elif target > row[-1]:
                l = mid_row + 1
            else:
                rowL, rowR = 0, len(row) - 1
                while rowL <= rowR:
                    mid = (rowL+rowR)//2
                    if target == row[mid]:
                        return True
                    elif target > row[mid]:
                        rowL = mid+1
                    else:
                        rowR = mid-1
                return False
        
        return False