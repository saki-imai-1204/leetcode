#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = set()
        squares = [set(), set(), set()]
        for i in range(9):
            row = set()
            if i % 3 == 0:
                squares = [set(), set(), set()]
            for j in range(9):
                if board[i][j] != "." and board[i][j] in row:
                    return False
                elif board[i][j] != ".": row.add(board[i][j])
                if board[i][j] != "." and board[i][j] in squares[j // 3]:
                    return False
                elif board[i][j] != ".": squares[j // 3].add(board[i][j])
        column = set()
        for i in range(9):
            column = set()
            for j in range(9):
                if board[j][i] != "." and board[j][i] in column:
                    return False
                elif board[j][i] != ".": column.add(board[j][i])
        
        return True
    
# Notes (6/10/2023)
# General idea:
# Use a set to track which numbers are in each row, column and squares
# 
# time complexity: O(n^2) 
# - going through the n x n matrix twice with O(1) operation inside the for loops
# 
# space complexity: O(n) -- 5 sets of a size at most O(n)
         
# @lc code=end

