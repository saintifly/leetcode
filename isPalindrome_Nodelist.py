# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def reverseList(head):
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

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        len_head = 0
        l1 = head
        while l1 != None:
            l1 = l1.next
            len_head = len_head + 1
        print len_head
        l1 = head
        len_half = 0 
        while len_half != ((len_head)/2):
            l1 = l1.next
            len_half = len_half + 1
        if len_head%2 != 0:
            l1=l1.next
        l1 = reverseList(l1)
        while l1 != None:
            if l1.val != head.val:
                return False
            l1 = l1.next
            head = head.next
        return True