# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pointCycle = head
        pointHis = []
        while (pointCycle !=None):
            if pointCycle not in pointHis:
                pointHis.append(pointCycle)
                pointCycle = pointCycle.next
            else:
                return pointCycle
        return None