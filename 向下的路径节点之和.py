# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        global sum
        pre_node = 0
        tmp = 0
        sum = 0
        path = [0]

        def inorder(root: Optional[TreeNode], pre_node):  ###求所有节点之各
            if root == None:
                return None
            root.val = root.val + pre_node
            pre_node = root.val
            inorder(root.left, pre_node)
            inorder(root.right, pre_node)

        inorder(root, pre_node)

        def inorderTraversal(root):
            """
            :type root: TreeNode
            :rtype: List[int]
            """
            if root is None: return []
            output = []
            output.append(root.val)
            output.extend(inorderTraversal(root.left))
            output.extend(inorderTraversal(root.right))
            return output

        ret1 = []
        ret1 = inorderTraversal(root)
        print(ret1)

        def binaryTreePaths(root: TreeNode, path):  ##求所有路径
            if (root == None):
                return 0
            result = traverse(root, path)
            return result

        def traverse(root: TreeNode, path):
            global sum

            if root == None:
                return path
            print(path, root.val)
            if root.val - targetSum in path:
                print(111, path, root.val)
                sum = sum + path.count(root.val - targetSum)
            path.append(root.val)
            if root.left != None:
                path = traverse(root.left, path)
            if root.right != None:
                path = traverse(root.right, path)
            path = path[:-1]
            return path

        binaryTreePaths(root, path)
        return sum
