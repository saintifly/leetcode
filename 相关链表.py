class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        headALen = 0
        headApoint = headA
        headBLen = 0
        headBpoint = headB
        distheadAB = 0
        resout = None
        while headApoint!= None:
            headALen += 1
            headApoint = headApoint.next
        while headBpoint!= None:
            headBLen += 1
            headBpoint = headBpoint.next
        headApoint = headA
        headBpoint = headB
        if headALen>= headBLen:
            distheadAB = headALen - headBLen
            for i in range(distheadAB):
                headApoint =  headApoint.next
        else:
            distheadAB = headBLen - headALen
            for i in range(distheadAB):
                headBpoint =  headBpoint.next
        while (headApoint!=None):
            if headApoint == headBpoint:
                resout = headApoint
                break
            headApoint = headApoint.next
            headBpoint = headBpoint.next
        return resout