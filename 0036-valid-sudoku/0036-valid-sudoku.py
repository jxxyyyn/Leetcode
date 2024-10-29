class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        
        for row in board:
            nums_in_row = [num for num in row if num != '.']
            if len(nums_in_row) != len(set(nums_in_row)):
                return False
        
        for col in range(9):
            nums_in_column = [board[row][col] for row in range(9) if board[row][col] != '.']
            if len(nums_in_column) != len(set(nums_in_column)):
                return False
        
        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                grid = set()
                for i in range(3):
                    for j in range(3):
                        num = board[row_start + i][col_start + j]
                        if num != '.' and num in grid:
                            return False
                        grid.add(num)
                        
        return True
