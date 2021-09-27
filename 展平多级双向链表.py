"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
def print_linked_list(head):
    if not head or not head.next:
        return []
    result = []    
    while head:
        result.append(head.val)
        head = head.next
    return result

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        pointA = head
        pointB = head
        pointC = head # 用于节点转换临时变量
        # print(print_linked_list(head))
        if head==None:
            return head
        while pointA.next != None or  pointA.child !=None:
            # print('11111',pointA.val,pointB.val)
            if pointA.child !=None:
                pointC = pointA.child
                pointB = pointA.next
                pointA.next = pointC
                pointA.child = pointB
                pointC.prev = pointA
                if pointB!= None:
                    pointB.prev = None
                # print('111111',print_linked_list(head))
            pointA = pointA.next
            pointB = pointA
            if pointA.next == None:
                while pointA.child==None:
                    if pointA.prev==None:
                        print(2222,pointA.val,pointB.val)
                        return head
                    pointA = pointA.prev
                pointB.next =  pointA.child
                pointA.child.prev = pointB
                pointA.child =None
                # print('22222',print_linked_list(head))
        