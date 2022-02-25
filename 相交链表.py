class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        headANum = 1
        headBnum = 1
        pointA= headA
        pointB = headB
        endCompare = 0
        skipA = 0
        skipB = 0
        while (pointA.next!=None):
            headANum = headANum + 1
            pointA = pointA.next
        while (pointB.next!= None):
            headBnum = headBnum + 1
            pointB = pointB.next
        if headBnum > headANum:
            endCompare = headANum
            skipB =  headBnum-headANum
        else:
            endCompare = headBnum
            skipA = headANum-headBnum
        pointA= headA
        pointB = headB
        for i in range(endCompare):
            while (skipA != 0):
                pointA =  pointA.next
                skipA = skipA - 1
            while (skipB != 0):
                pointB = pointB.next
                skipB =skipB -1
            if pointA is pointB:
                return pointA
            else:
                pointA = pointA.next
                pointB = pointB.next
        return None
