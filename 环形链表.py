# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        if head.next == None:
            return False           
        hash_List=[]
        while head != None:
            hash_Node = hash(head)
            if  hash_Node not in hash_List:
                hash_List.append(hash_Node)
                head =  head.next
            else:
                return True
        if head==None:
            return False