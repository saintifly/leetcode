class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        from collections import deque
        q_bfs = deque()
        m = len(graph)
        n = len(graph[0])
        visted = [0]
        clourSet =  [0 for j in range(m)]
        for i in range(m):
            if clourSet[i]==0:		
                clourSet[i]=1
                q_bfs.append(i)
                while q_bfs:
                    k = q_bfs.popleft()
                    for j in graph[k]:
                        if j in visted:
                            if clourSet[j] == clourSet[k]:
                                return False
                            else:
                                continue
                        else:
                            if clourSet[j] ==0:
                                if clourSet[k]==1:
                                    clourSet[j] = 2
                                if clourSet[k]==2:
                                    clourSet[j] = 1
                                visted.append(j)
                                q_bfs.append(j)
        return True