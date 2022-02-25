class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        if head.next.next==None:
            headcurrent=head
            head=head.next
            headcurrent.next=None
            head.next=headcurrent
            return head
        headbefore=None
        headcurrent=head
        headnext=headcurrent.next
        headcurrent.next=headbefore
       
        
        while headnext.next!=None:
            headbefore=headcurrent
            headcurrent=headnext
            headnext=headnext.next
            headcurrent.next=headbefore
        headcurrent.next=headbefore    
        headnext.next=headcurrent 
        return headnext
            