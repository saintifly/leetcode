# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        pointNow = head
        pointBefore = None
        pointAfter = head.next
        while(pointNow.next!=None):
            pointNow.next =pointBefore
            pointBefore = pointNow
            pointNow = pointAfter
            pointAfter =pointAfter.next
        pointNow.next = pointBefore
        head =pointNow
        return head


