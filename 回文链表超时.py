# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        print(head)
        if head is None:
            return False
        pointEnd = head.next
        pointEndbefor = head
        if pointEnd!=None:
            while(pointEnd.next!=None):
                pointEnd =  pointEnd.next
                pointEndbefor = pointEndbefor.next
        else:
            return True
        if head.val == pointEnd.val:
            if head.next == pointEnd:
                return True
            pointEndbefor.next = None
            return self.isPalindrome(head.next)
        return False