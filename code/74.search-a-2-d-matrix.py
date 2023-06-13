#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            if self.binary_search(matrix[row], target, 0, len(matrix[row])-1):
                return True
        else:
            return False
        
    def binary_search(self, list, target, start, end):
        if start > end:
            return False
        mid = start + (end - start) // 2
        if target == list[mid]: return True
        elif target > list[mid]: return self.binary_search(list, target, mid + 1, end)
        else: return self.binary_search(list, target, start, mid - 1)


# Notes (6/13/2023)
# Run a binary search on each of the row to check if a number exists 

# time complexity - O(m * log n)

# Improved solution:
# Run a binary search to figure out which row could contain a target, and 
# run a binary search again to see if a target exists in that row

# time complexity - O(log m * log n)
        
# @lc code=end

