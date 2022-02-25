# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None:
            return l2
        if l2==None:
            return l1
        if l1.val<=l2.val:
            l3=l1
            l4=l1.next
            #l1.next=l2
            l5=l2
            l6=l1
        else:
            l3=l2
            l5=l2.next
            #l2.next=l1
            l4=l1
            l6=l2
        
        while l4!=None or l5!=None:
            if l4==None:
                l6.next=l5
                break
            if l5==None:
                l6.next=l4
                break
            if l4.val<=l5.val:
                l6.next=l4
                l6=l4
                l4=l4.next
                #l6.next=l5
                #l6=l5
                #l5=l5.next
            else:
                l6.next=l5
                l6=l5
                l5=l5.next
                #.next=l4
                #l6=l4
                #l4=l4.next
                
        return l3