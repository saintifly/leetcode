class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cityNum = len(isConnected)
        cityVisted = [0]*cityNum
        def dfs(i):
            for j in range(cityNum):
                if isConnected[i][j]==1 and cityVisted[j]==0:
                    cityVisted[j]=1
                    dfs(j)

        circles = 0

        for i in range(cityNum):
            if cityVisted[i]==0:
                dfs(i)
                circles += 1
        return circles