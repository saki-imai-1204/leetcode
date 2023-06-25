#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative
        prev, curr = None, head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev

        # Recursivce
        if not head:
            return head
        else:
            newhead = head
            if head.next:
                newhead = self.reverseList(head.next)
                head.next.next = head
            head.next = None
            
            return newhead

# Notes (6/24/2023)
# Iterative solution:
# Take the prev pointer and the current pointer
# Change the pointer one by one as you go through each element in the while loop
# time complexity: O(n)
# space complexity: O(1) -- two pointers

# Recursive solution:
# Idea: reverse from the back one by one
# time complexity: O(n)
# space complexity: O(n) 
# @lc code=end

