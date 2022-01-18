class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)  #0到n-1所有路径
        global resultList, path
        resultList = []
        path = [0]

        def dfsSub(graph, startIndex):
            global path, resultList
            if startIndex == n-1:
                resultList.append(path)
                return
            for i in graph[startIndex]:
                path.append(i)
                dfsSub(graph,i)
                path = path[:-1]
            return resultList

        dfsSub(graph, 0)
        return resultList