class Solution:
    def isSimilarStr(self,str1,str2):
        diff = 0
        for i,item in enumerate(str1):
            if item!= str2[i]:
                diff = diff+1
        if diff<3:
            return True
        else:
            return False

    def findCircleNum(self,isConnected: List[List[int]]) -> int:
        '''
        dfs：遍历所有城市，如果有1或者访问过，pass

        isConnected:各个城市的连接状态
        :param isConnected:
        :return:
        '''
        cityNum = len(isConnected)
        cityVisted = [0] * cityNum

        def dfs(i):
            for j in range(cityNum):
                if isConnected[i][j] == 1 and cityVisted[j] == 0:
                    cityVisted[j] = 1
                    dfs(j)

        circles = 0

        for i in range(cityNum):
            if cityVisted[i] == 0:
                dfs(i)
                circles += 1
        return circles

    def numSimilarGroups(self, strs: List[str]) -> int:
        num =  len(strs)
        similarGrap=[[0]*num for i in range(num)]
        for i,item in enumerate(strs):
            for j,item1 in enumerate(strs):
                if self.isSimilarStr(item,item1) is True:
                    similarGrap[i][j]=1
                else:
                    similarGrap[i][j] = 0
        ret =self.findCircleNum(similarGrap)
        return retclass Solution:
    def isSimilarStr(self,str1,str2):
        diff = 0
        for i,item in enumerate(str1):
            if item!= str2[i]:
                diff = diff+1
        if diff<3:
            return True
        else:
            return False

    def findCircleNum(self,isConnected: List[List[int]]) -> int:
        '''
        dfs：遍历所有城市，如果有1或者访问过，pass

        isConnected:各个城市的连接状态
        :param isConnected:
        :return:
        '''
        cityNum = len(isConnected)
        cityVisted = [0] * cityNum

        def dfs(i):
            for j in range(cityNum):
                if isConnected[i][j] == 1 and cityVisted[j] == 0:
                    cityVisted[j] = 1
                    dfs(j)

        circles = 0

        for i in range(cityNum):
            if cityVisted[i] == 0:
                dfs(i)
                circles += 1
        return circles

    def numSimilarGroups(self, strs: List[str]) -> int:
        num =  len(strs)
        similarGrap=[[0]*num for i in range(num)]
        for i,item in enumerate(strs):
            for j,item1 in enumerate(strs):
                if self.isSimilarStr(item,item1) is True:
                    similarGrap[i][j]=1
                else:
                    similarGrap[i][j] = 0
        ret =self.findCircleNum(similarGrap)
        return ret