# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p=head
        q=head
        
        if p.next==None and n==1:
            return None
        
        for i in range(n):
            p=p.next

        while p!= None:
            p=p.next
            if q.next.next == None:
                q.next=None
            else:
                q=q.next

        print q
        if q.next == None:
            q=None
        else:
            q.val =q.next.val
            q.next = q.next.next      
        return head  