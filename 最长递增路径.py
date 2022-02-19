class Solution:
    def dps(self,grid,i,j,Nodebefore):
            global tmp,m,n,visted,maxOut
            if len(tmp)>=2 and tmp[-1] <= tmp[-2]:
                    tmp = tmp[:-1]
            if grid[i][j] > Nodebefore:
                if len(tmp)>=2 and Nodebefore!=tmp[-1]:
                    for k in range(len(tmp)):
                        if Nodebefore == tmp[-k]:
                            tmp[-k+1]=grid[i][j]
                            tmp = tmp[:-k+1]+[tmp[-k+1]]
                            break
                else:
                    tmp.append(grid[i][j])
            if len(tmp) > maxOut:
                maxOut = len(tmp)
            Nodebefore = grid[i][j]
            for k in range(4):
                if k==0:
                    i = i+1
                    if  i<0 or i>m-1 or j <0 or j>n-1 or grid[i][j]<=grid[i-1][j] :
                        i=i-1
                        visted[i][j] = visted[i][j] + 1
                        continue
                    else:
                        self.dps(grid,i,j,Nodebefore)
                        i=i-1
                        if visted[i][j] == 4 :
                            return maxOut

                if k==1:
                    j = j+1
                    if  i<0 or i>m-1 or j <0 or j>n-1 or grid[i][j]<=grid[i][j-1] :
                        j=j-1
                        visted[i][j] = visted[i][j] + 1
                        continue
                    else:
                        self.dps(grid,i,j,Nodebefore)
                        j = j - 1
                        if visted[i][j] == 4 :
                            return maxOut

                if k==2:
                    i = i-1
                    if  i<0 or i>m-1 or j <0 or j>n-1 or grid[i][j]<=grid[i+1][j] :
                        i=i+1
                        visted[i][j] = visted[i][j] + 1
                        continue
                    else:
                        self.dps(grid,i,j,Nodebefore)
                        i=i+1
                        if visted[i][j] == 4 :
                            return maxOut
                if k==3:
                    j = j-1
                    if  i<0 or i>m-1 or j <0 or j>n-1 or grid[i][j]<=grid[i][j+1] :
                        j=j+1
                        visted[i][j] = visted[i][j] + 1
                        return maxOut
                    else:
                        self.dps(grid,i,j,Nodebefore)
                        j = j + 1
                        if visted[i][j] == 4 :
                            return maxOut
            return maxOut

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        global m,n,tmp,visted,maxOut,Nodebefore
        m = len(matrix)
        n = len(matrix[0])
        ret = []
        temp = 0
        for i in range(m):
            for j in range(n):
                tmp = [matrix[i][j]]
                maxOut =1
                Nodebefore = matrix[i][j]
                visted =  [[0 for i in range(n)] for j in range(m)]
                ret = self.dps(matrix,i,j,Nodebefore)
                temp =max(ret,temp)
        return temp
