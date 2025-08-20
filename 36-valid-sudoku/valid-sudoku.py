from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for i in range(9):
            row_map = set()
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    if num in row_map:
                        return False
                    row_map.add(num)

        # Check columns
        for i in range(9):
            col_map = set()
            for j in range(9):
                num = board[j][i]
                if num != ".":
                    if num in col_map:
                        return False
                    col_map.add(num)

        # Check 3x3 sub-grids
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box_map = set()
                for i in range(3):
                    for j in range(3):
                        num = board[box_row + i][box_col + j]
                        if num != ".":
                            if num in box_map:
                                return False
                            box_map.add(num)

        return True
