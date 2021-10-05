# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        levelOut = []
        levelNodeList = []
        levelmax = []
        levelNodeListNext = []
        currentLevelTree = root
        levelNodeList.append(currentLevelTree)
        n=1
        if root ==None:
            return []
        tmp = 0
        while(levelNodeList!=[]):
            if tmp ==0 :
                levelmax.append(levelNodeList[0].val)
                if levelNodeList[0].left!=None:
                    levelNodeListNext.append(levelNodeList[0].left)
                tmp = 1
            else:
                if levelNodeList[0].right!=None:
                    levelNodeListNext.append(levelNodeList[0].right)
                levelNodeList.remove(levelNodeList[0])
                tmp = 0
                n = n-1
            if levelNodeList ==[] or n==0:
                levelOut.append(max(levelmax))
                levelmax = []
                if levelNodeListNext!=[]:
                    levelNodeList =  levelNodeListNext
                    n =len(levelNodeListNext)  
        return levelOut  