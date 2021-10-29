class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
            global resultList,path,path1,path2,path3
            resultList = []
            path = ''
            path1 = ''
            path2 = ''
            path3 = []
            def dfsSub(n):
                global path,resultList,path1,path2,path3
                if len(path)>=n*2 or len(path1)>n or len(path2)>n or len(path2)>len(path1):
                      print(path)
                      print("11111111",path3)
                      if path3 ==[] and len(path) ==2*n:
                          resultList.append(path)
                      return
                for i in range(2):
                    if i==0:
                        path1 = path1 + "("
                        path =  path + "("
                        path3.append("1")
                    else:
                        path2 = path2 + ")"
                        path =  path + ")"
                        if path3!=[]:
                            path3.pop()
                    dfsSub(n)
                    if path[-1]=='(':
                        path1 = path1[:-1]
                        path =  path[:-1]
                        if path3!=[]:
                            path3.pop()
                    else:
                        path2 = path2[:-1]
                        path =  path[:-1]
                        if len(path1)<=len(path2):
                            path3.append('1')
                return resultList
            dfsSub(n)
            return resultList
