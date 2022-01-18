class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        locklen = len(target)
        start = '0'*locklen
        if start in deadends:
            return -1
        if start==target:
            return 0
        start_bfs_deq =  deque()
        start_bfs_deq.append(start)
        startdis = {}
        startdis[start] = 0
        dir_num = ['0','1','2','3','4','5','6','7','8','9','0','9']

        end = target
        end_bfs_deq = deque()
        end_bfs_deq.append(target)
        enddis = {}
        enddis[end] = 0

        while start_bfs_deq and end_bfs_deq:
            currentNode = start_bfs_deq.popleft()
            for j in range(locklen):
                NodeNum = int(currentNode[j])
                disNum = startdis[currentNode]
                if j+1<=locklen-1:
                    currentNode_last = currentNode[j+1:]
                else:
                    currentNode_last=''
                currentNode = currentNode[:j]+ dir_num[NodeNum+1] +currentNode_last
                if currentNode not in deadends and currentNode not in startdis.keys():
                    startdis[currentNode] = disNum +1
                    start_bfs_deq.append(currentNode)
                if currentNode in enddis.keys():
                    return startdis[currentNode]+enddis[currentNode]
                currentNode = currentNode[:j]+ dir_num[NodeNum-1] +currentNode_last
                if currentNode not in deadends and currentNode not in startdis.keys():
                    startdis[currentNode] = disNum +1
                    start_bfs_deq.append(currentNode)
                if currentNode in enddis.keys():
                    return startdis[currentNode]+enddis[currentNode]
                currentNode = currentNode[:j]+ dir_num[NodeNum] +currentNode_last

            currentNode = end_bfs_deq.popleft()
            for j in range(locklen):
                NodeNum = int(currentNode[j])
                disNum = enddis[currentNode]
                if j+1<=locklen-1:
                    currentNode_last = currentNode[j+1:]
                else:
                    currentNode_last=''
                currentNode = currentNode[:j]+ dir_num[NodeNum+1] +currentNode_last
                if currentNode not in deadends:
                    enddis[currentNode] = disNum + 1
                    end_bfs_deq.append(currentNode)
                if currentNode in startdis.keys():
                    return startdis[currentNode] + enddis[currentNode]
                currentNode = currentNode[:j] + dir_num[NodeNum - 1] + currentNode_last
                if currentNode not in deadends:
                    enddis[currentNode] = disNum + 1
                    end_bfs_deq.append(currentNode)
                if currentNode in startdis.keys():
                    return startdis[currentNode] + enddis[currentNode]
                currentNode = currentNode[:j]+ dir_num[NodeNum] +currentNode_last
        return -1