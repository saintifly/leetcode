#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        bfs_tmp=[root]
        res = []
        res_unit =[]
        while bfs_tmp !=[]:
            res_unit=[]
            num = len(bfs_tmp)
            for i in range(num):
                bfs_one = bfs_tmp.pop(0)
                if bfs_one is not None:
                    res_unit.append(bfs_one.val)
                    if bfs_one.left is not None:
                        bfs_tmp.append(bfs_one.left)
                    if bfs_one.right is not None:
                        bfs_tmp.append(bfs_one.right)
            res.append(res_unit)
        return res