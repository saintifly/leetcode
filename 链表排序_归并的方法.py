# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
    def mergeKListsTwo(self, list1,list2):
        '''
        使用归并的思想中的并处理
        '''
        p0 = list1
        p1 = list2
        h0 = ListNode(-1)
        h = h0
        while(p0!=None and p1!=None):
            if p0.val < p1.val:
                h.next = p0
                p0 = p0.next
            else:
                h.next = p1
                p1 = p1.next
            h = h.next
        if (p0!=None):
            h.next = p0
        if (p1!=None):
            h.next = p1
        return h0.next

    def midOfNode(self,head):
        '''
        链表拆分成两半，返回后半部分
        '''
        
        p0 = head
        p1 = head.next

        while( p1!=None and p1.next!=None):
            p0 = p0.next
            p1 = p1.next.next
        p1 = p0.next
        p0.next = None
        return p1
    
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if ( head==None or head.next ==None):
             return head
        p1 =  self.midOfNode(head)
        p1 = self.sortList(p1)
        head = self.sortList(head)
        ret = self.mergeKListsTwo(head,p1)
        return ret 