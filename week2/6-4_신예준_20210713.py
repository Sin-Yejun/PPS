# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        li = []
        curr = head
        while curr!= None:
            li.append(curr.val)
            curr = curr.next
        if li == li[::-1]:
            return True
        else:
            return False
