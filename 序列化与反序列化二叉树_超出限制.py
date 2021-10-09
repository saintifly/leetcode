# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        list_dynicm = []
        list_dynicm.append(root)
        retList = []
        if root ==None:
            return []
        P0= root
        while(list_dynicm!=[]):
            if list_dynicm[0] !='null':
                P0 = list_dynicm[0]
                retList.append(P0.val)
            else:
                retList.append("null")
                list_dynicm = list_dynicm[1:]
                continue
            if P0.left!=None:
                list_dynicm.append(P0.left)
            else:
                list_dynicm.append('null')
            if P0.right!=None:
                list_dynicm.append(P0.right)
            else:
                list_dynicm.append('null')
            list_dynicm = list_dynicm[1:]
        return retList

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        LineList  =  []
        LineListBefore = []
        n = 1
        root  =  None
        flag =0
        print(data)
        for i in data:
            if i!='null':
                Tmp_Node = TreeNode(i)
                LineList.append(Tmp_Node)
            else:
                LineList.append(None)
            if len(LineList)==n:
                print('LineList',LineList,n)
                for i in LineList:
                    print('root',root)
                    print('i',i,n)
                    print('Linelistbefor',LineListBefore)
                    if  root ==None:
                        root = i
                        LineList = LineList[1:]
                        LineListBefore.append(i)
                        break
                    else:
                        while LineListBefore[0]==None:
                            LineListBefore =LineListBefore[1:]
                        if flag ==0:
                            # if i== None:
                            #     flag = 1
                            #     LineList = LineList[1:]
                            #     continue
                            LineListBefore[0].left = i
                            LineListBefore.append(LineList[0])
                            LineList = LineList[1:]
                            flag  =1       
                        else:
                            # if i== None:
                            #     LineListBefore = LineListBefore[1:]
                            #     LineList = LineList[1:]
                            #     continue
                            LineListBefore[0].right = i
                            flag = 0
                            LineListBefore = LineListBefore[1:]
                            LineListBefore.append(LineList[0])
                            LineList = LineList[1:]
                if 2*n>len(LineListBefore):
                    n = len(LineListBefore)
                else:
                    n=2*n
                continue
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))