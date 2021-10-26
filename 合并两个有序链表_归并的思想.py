# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKListsTwo(self, list1,list2):
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

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists==[]:
            return None
        if len(lists)<2:
            return lists[0]
        tmp = lists[0]
        for i in lists[1:]:
                tmp = self.mergeKListsTwo(tmp,i)
        return tmp

    