class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        from collections import deque
        from typing import List
        from math import sqrt
        m = len(mat)
        n = len(mat[0])
        ret = [[0 for i in range(n)] for j in range(m)]
        def MaxDistanBFS(mat,i,j):
            bfs_deq = deque()
            bfs_deq.append([i,j])
            visted=[]
            visted.append([i,j])
            i0 = i
            j0 = j
            while(bfs_deq):
                [i,j] = bfs_deq.popleft()
                ret =  math.ceil(sqrt(abs(i-i0)**2+abs(j-j0)**2))+1
                for k in range(4):
                    if k==0:
                        if i+1>m-1:
                            continue
                        if mat[i+1][j]==0:
                            return ret
                        if [i+1,j] not in visted:
                            bfs_deq.append([i+1,j])
                            visted.append([i+1,j])
                    if k==1:
                        if j+1>n-1:
                            continue
                        if mat[i][j+1]==0:
                            return ret
                        if [i,j+1] not in visted:
                            bfs_deq.append([i,j+1])
                            visted.append([i,j+1])
                    if k==2:
                        if i-1<0:
                            continue
                        if mat[i-1][j]==0:
                            return ret
                        if [i-1,j] not in visted:
                            bfs_deq.append([i-1,j])
                            visted.append([i-1,j])
                    if k==3:
                        if j-1<0:
                            continue
                        if mat[i][j-1]==0:
                            return ret
                        if [i,j-1] not in visted:
                            bfs_deq.append([i,j-1])
                            visted.append([i,j-1])
            return ret
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    continue
                if mat[i][j]==1:
                    ret[i][j] = MaxDistanBFS(mat,i,j)
        return ret 