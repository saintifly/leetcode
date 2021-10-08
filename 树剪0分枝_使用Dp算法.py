# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        ###DP算法
        Two_Path = [0, 1]
        TreeNode_P0 = root
        TreeNode_P1 = root
        # for i in TreeNode:
        #     if
        root_path = []
        root_path.append(root)
        n = 1
        flag = 0
        if root==None:
            return None
        if root.left == None:
            flag = flag + 1
        flag1=0
        while (TreeNode_P0 != root or flag != 3):
            if TreeNode_P0 == root:
                flag = flag+1
            if TreeNode_P0.left == None and TreeNode_P0.right == None and TreeNode_P0.val==0:
                root_path.remove(TreeNode_P0)
                if TreeNode_P1.left == TreeNode_P0:
                    TreeNode_P1.left=None
                else:
                    TreeNode_P1.right = None
                if TreeNode_P0 == root:
                    return None
                TreeNode_P0 =TreeNode_P1
                n=1
            if TreeNode_P0.left !=None and TreeNode_P0.left not in root_path:
                root_path.append(TreeNode_P0.left)
                TreeNode_P1 = TreeNode_P0
                TreeNode_P0 = root_path[-1]
                n=1
                flag1 = 1
                continue
            elif TreeNode_P0.right !=None and TreeNode_P0.right  not in root_path:
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

        return root