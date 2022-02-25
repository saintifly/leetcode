# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pointDelNode = head
        pointEndNode = head
        while (n != 0):
            pointEndNode = pointEndNode.next
            n = n - 1
        if pointEndNode != None:
            while (pointEndNode.next != None):
                pointEndNode = pointEndNode.next
                pointDelNode = pointDelNode.next
            if pointDelNode.next == pointEndNode:
                pointDelNode.next = None
                return head
        if pointDelNode == head and pointEndNode == None:
            print(pointDelNode, pointEndNode)
            head = head.next
            pointEndNode = pointDelNode
        else:
            print(pointDelNode, pointEndNode)
            pointEndNode = pointDelNode.next
            pointDelNode.next = pointEndNode.next
        pointEndNode.next = None
        del pointEndNode
        return head




