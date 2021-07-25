# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        curr = head
        ct = 0
        while(curr):
            ct +=1
            curr = curr.next
        if ct % 2 == 1:
            x = ct//2+1
        else:
            x = ct//2
        li = []
        curr1 = head
        check = 0
        
        while(curr1):
            check +=1
            if x < check:
                head = head.next
            curr1 = curr1.next
        return head
