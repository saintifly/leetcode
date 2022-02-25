# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reveseLink(self,head:ListNode)->ListNode:
        if head == None or head.next ==None:
            return head
        pointCurrent = head
        pointNext = head.next
        pointBefore = None
        while(pointCurrent.next!=None):
            pointCurrent.next = pointBefore
            pointBefore = pointCurrent
            pointCurrent = pointNext
            pointNext = pointNext.next
        pointCurrent.next = pointBefore
        return pointCurrent

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # pointFirstCur = head
        # pointFirstNex = head.next
        # pointInsert = self.reveseLink(head)
        # print('999',head.next)
        # while(pointInsert != head):
        #     pointFirstCur.next = pointInsert
        #     pointFirstCur =  pointInsert.next
        #     pointFirstCur.next.next = pointFirstNex
        #     pointInsert = pointFirstCur
        #     pointFirstCur = pointFirstNex
        #     self.reveseLink(head)
        #     pointFirstNex = pointFirstNex.next
        #     print('45678',pointFirstCur.val)
        # return head
        pointA = head
        n = 0
        half_n = 0
        pointB = head
        while (pointA!=None):
            n = n +1
            pointA = pointA.next
        if n<=2:
            return head
        if n%2 ==0:
            half_n = n//2-1
        else:
            half_n = n//2
        for i in range(half_n):
            pointB = pointB.next
        pointC = self.reveseLink(pointB.next)
        pointB.next =None
        pointA = head
        pointB = pointC
        pointD = head
        while (pointD != None):
            pointD = pointA.next
            pointA.next = pointB
            pointA = pointB.next
            pointB.next = pointD
            pointB = pointA
            pointA = pointD
            pointD = pointD.next
        pointA.next = pointB
        return head