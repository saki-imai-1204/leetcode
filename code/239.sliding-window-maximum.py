#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        l = r = 0
        q = collections.deque() 

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r+1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output

# Notes (6/9/2023)
# General idea:
# Use deque (monotonically decreasing queue)
#   - since O(1) for adding, removing and popping
# Use a sliding window l, r
# Iterate through the array with the right pointer of the sliding window
#   while q is not empty and the right most element of the queue is
#   smaller than the current element
#       pop the last element
#   if the left pointer is out of the sliding window, 
#       pop left
#   if the length of the window reached k
#       start adding the left most element to the output array
#       increment the left pointer

# time complexity: O(n) 
#   - adding and popping in both O(1)
#   - we do it for n times

# space complexity: O(n) 
#   - creating a deque of size at most n

        
# @lc code=end

