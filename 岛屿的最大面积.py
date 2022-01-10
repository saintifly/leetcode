class Solution:
    def dps(self,grid,i,j):
        global tmp,m,n,visted
        if grid[i][j]==1 and visted[i][j]==0:
             tmp=tmp+1
        if visted[i][j]==5:
            return tmp
        else:
            visted[i][j] = visted[i][j] + 1
        for k in range(4):
            if k==0:
                i = i+1
                if  i<0 or i>m-1 or j <0 or j>n-1 or grid[i][j]==0 or visted[i][j]>0:
                    i=i-1
                    visted[i][j] = visted[i][j] + 1
                    continue
                else:
                    self.dps(grid,i,j)
                    i=i-1
                    if visted[i][j] == 4 :
                        return tmp

            if k==1:
                j = j+1
                if  i<0 or i>m-1 or j <0 or j>n-1 or grid[i][j]==0 or visted[i][j]>0:
                    j=j-1
                    visted[i][j] = visted[i][j] + 1
                    continue
                else:
                    self.dps(grid,i,j)
                    j = j - 1
                    if visted[i][j] == 4 :
                        return tmp

            if k==2:
                i = i-1
                if  i<0 or i>m-1 or j <0 or j>n-1 or grid[i][j]==0 or visted[i][j]>0:
                    i=i+1
                    visted[i][j] = visted[i][j] + 1
                    continue
                else:
                    self.dps(grid,i,j)
                    i=i+1
                    if visted[i][j] == 4 :
                        return tmp
            if k==3:
                j = j-1
                if  i<0 or i>m-1 or j <0 or j>n-1 or grid[i][j]==0 or visted[i][j]>0:
                    j=j+1
                    visted[i][j] = visted[i][j] + 1
                else:
                    self.dps(grid,i,j)
                    j = j + 1
                    if visted[i][j] == 4 :
                        return tmp
        return tmp

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        global m,n,tmp,visted
        m = len(grid)
        n = len(grid[0])
        visted =  [[0 for i in range(n)] for j in range(m)]
        maxRet = 0
        ret = 0
        tmp = 0
        for i in range(m):
            for j in range(n):
                if visted[i][j]==0 and grid[i][j]==1:
                    ret = self.dps(grid,i,j)
                maxRet = max(ret,maxRet)
                tmp=0
        return maxRet