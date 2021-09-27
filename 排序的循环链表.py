"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if head == None:
            pointA = Node(insertVal)
            pointA.next = pointA
            return pointA
        pointA =head
        pointB = head
        pointC = head
        maxNode = -10^6
        while(True):
            if (pointA.val<=insertVal and pointA.next.val>=insertVal):
                pointB = pointA
                break
            pointA = pointA.next
            if pointA.val >=maxNode:
                maxNode = pointA.val
                pointC =  pointA
            if pointA == pointB:
                pointB = pointC
                break
        insertNode = Node(insertVal)
        pointA = pointB.next
        insertNode.next = pointA
        pointB.next = insertNode
        return head