#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False

# Note (6/27/2023): 
# Idea 1 – time complexity: O(n), space complexity: O(n) solution
#   - Use hashmap
# Idea 2 – time complexity: O(n), space complexity: O(1) solution
#   - Use Floyd’s Tortoise and Hare algorithm
#   - Basically, we will prepare a fast and a slow pointer where a faster pointer 
#   moves ahead by 2 and a slow pointer moves ahead by 1
#   - Then, if there exists a cycle, then the two pointers meet each other after n steps
#   - Since for each iteration, the gap shrinks by 1
    
# @lc code=end

