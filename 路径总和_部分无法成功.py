# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
         ###DP算法
        TreeNode_P0 = root
        TreeNode_P1 = root
        # for i in TreeNode:
        #     if
        root_path = []
        root_path.append(root)
        n = 1
        flag = 0
        if root==None:
            return 0
        if root.left==None and root.right==None:
            if root.val==targetSum:
                return 1
        if root.left == None:
            flag = flag + 1
        flag1=0
        retlist = []
        retlist.append(root.val)
        count = 0
        flag2 = 0
        if root.val==targetSum:
           count =count+1
        while (TreeNode_P0 != root or flag != 3):
            if TreeNode_P0 == None:
                continue
            if TreeNode_P0 == root:
                flag = flag+1
            if flag ==2 and flag2 ==0:
                print('0000000')
                retlist=[root.val]
                flag2 =1
            print(retlist,TreeNode_P0.val)
            if TreeNode_P0.left !=None and TreeNode_P0.left not in root_path:
                if TreeNode_P0.left!=None:
                    TreeNode_P0.left.val = TreeNode_P0.left.val+TreeNode_P0.val
                    retlist.append(TreeNode_P0.left.val)
                    if TreeNode_P0.left.val-targetSum in retlist:
                        print('11111111',retlist,TreeNode_P0.left.val,count)
                        count = count+ retlist[:-1].count(TreeNode_P0.left.val-targetSum)
                        if targetSum==0  and TreeNode_P0.left.val-targetSum not in retlist[0:-1]:
                            print(-11111111)
                            count = count -retlist[:-1].count(TreeNode_P0.left.val-targetSum)

                    
                    if TreeNode_P0.left.val==targetSum:
                        print('222222',retlist,TreeNode_P0.left.val)
                        count +=1
                root_path.append(TreeNode_P0.left)
                TreeNode_P1 = TreeNode_P0
                TreeNode_P0 = root_path[-1]
                n=1
                flag1 = 1
                continue
            elif TreeNode_P0.right !=None and TreeNode_P0.right  not in root_path:
                print('llllllllllllll')
                if TreeNode_P0.right!=None:
                    TreeNode_P0.right.val = TreeNode_P0.right.val + TreeNode_P0.val
                    retlist.append(TreeNode_P0.right.val)
                    if TreeNode_P0.right.val-targetSum in retlist:
                        print('11111111',retlist,TreeNode_P0.right.val)
                        count = count +retlist[:-1].count(TreeNode_P0.right.val-targetSum)
                        if targetSum==0  and TreeNode_P0.right.val-targetSum not in retlist[0:-1]:
                            print(-11111111)
                            count = count -retlist[:-1].count(TreeNode_P0.right.val-targetSum)
                    if TreeNode_P0.right.val==targetSum:
                        print('222222',retlist)
                        count +=1
                root_path.append(TreeNode_P0.right)
                TreeNode_P1 = TreeNode_P0
                TreeNode_P0 = root_path[-1]
                flag1 = 2
                n=1
                continue
            # elif TreeNode_P0 in root_path:
            else:
                if n<=len(root_path):
                    TreeNode_P0 = root_path[-n]
                else:
                    TreeNode_P0 = root_path[0]
                if n+1 <=len(root_path):
                    TreeNode_P1 = root_path[-n-1]
                n = n+1
                if retlist!=[]:
                    i=0
                    if retlist[-1]!=TreeNode_P0.val and  n+1 <=len(root_path):
                        TreeNode_P0 = root_path[-n-i]
                        i=i+1
                #####这里有问题，回溯路径时，无法正常剪枝取值
                        
                if n>2 and n<len(root_path):
                    retlist = retlist[:-1]
                if retlist!=[]:
                    if n==len(root_path) and TreeNode_P0.val !=retlist[-1]:
                        retlist = retlist[:-1]
                #####这里有问题，回溯路径时，无法正常剪枝取值

        return count