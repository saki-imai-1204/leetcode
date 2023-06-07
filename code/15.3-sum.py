#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        for i in range(len(nums)-1):
            if (i == 0) or (i != 0 and nums[i-1] != nums[i]):
                l, r = i+1, len(nums)-1
                while (l < r):
                    if nums[i] + nums[l] + nums[r] > 0:
                        r -= 1
                    elif nums[i] + nums[l] + nums[r] < 0:
                        l += 1
                    else:
                        ans.append([nums[i], nums[l], nums[r]])
                        l += 1
                        while nums[l] == nums[l-1] and l < r:
                            l += 1 
        return ans


# Notes (6/6/2023)
# General idea:
# Basically the same idea as 167. Two Sum II - Input Array Is Sorted 
# but sort the array first and keep an additional left pointer that 
# chooses the first item to be added

# Steps:
# Sort the array
# Iterate through the list and skip the repeating element:
#   Calculate the three sum
#   If three sum > 0 then increment the left pointer
#   If three sum < 0 then decrement the right pointer
#   Else, append the result to the array and update the pointer
#   (This update of pointer can be done by, updating either 
#   the left or the right pointer and making sure that you are 
#   skipping the duplicate element)

# time complexity: O(nlogn) + O(n^2) = O(n^2)
# - O(nlogn) for sorting
# - O(n^2) for for loop + finding the two elements

# space complexity: either O(1) or O(n), depending on the sorting algorithm

# @lc code=end

