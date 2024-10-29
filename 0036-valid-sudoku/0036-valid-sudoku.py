class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        
        for row in board:
            seen = set()
            for num in row:
                if num != '.' and num in seen:
                    return False
                seen.add(num)
        
        for col in range(9):
            seen = set()
            for row in range(9):
                num = board[row][col]
                if num != '.' and num in seen:
                    return False
                seen.add(num)
        
        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        num = board[row_start+i][col_start+j]
                        if num != '.' and num in seen:
                            return False
                        seen.add(num)
                        
        return True