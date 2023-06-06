#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        freq = [[] for i in range(len(nums) + 1)]

        for n, c in hashmap.items():
            freq[c].append(n)
        
        ans = []
        for i in range(len(freq)-1, -1, -1):
            for j in freq[i]:
                if k > 0:
                    ans.append(j)
                    k -= 1
        return ans


# Notes (6/5/2023)

# Potential solution: Use max heap
# For each element, count the number of occurrences and put them in a set
# We don’t have to sort the whole hashmap because we only want the top k elements
# Heapify() can be done in linear time
# Each pop will be O(logn)
# So, the time complexity is O(k*logn)

# Solution in linear time:
# Use an array where the position represents a count and the value represent the number
# Notice that the size of the array is bounded to n where n is the number of elements in the input
# time complexity: O(n)
# space complexity: O(n)
#   - Array and hashmap to count the occurrences of each value

        
# @lc code=end

