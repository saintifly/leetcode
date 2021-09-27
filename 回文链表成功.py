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

    def isPalindrome(self, head: ListNode) -> bool:
        pointA = head
        n = 0
        half_n = 0
        pointB = head
        while (pointA != None):
            n = n + 1
            pointA = pointA.next
        if n % 2 == 0:
            half_n = n // 2 - 1
        else:
            half_n = n // 2
        for i in range(half_n):
            pointB = pointB.next
        pointC = self.reveseLink(pointB.next)
        pointA = head
        while (pointC !=None):
            if pointC.val != pointA.val:
                return False
            pointC = pointC.next
            pointA = pointA.next
        return True