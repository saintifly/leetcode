class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordIDList = dict()
        edge = collections.defaultdict(list)
        NodeID = 0
        def addword(word:str):
            nonlocal NodeID
            if word not in wordIDList:
                wordIDList[word]=NodeID
                NodeID = NodeID+1

        def addedg(word:str):
            addword(word)
            id1 = wordIDList[word]
            wordchar = list(word)
            for i in range(len(wordchar)):
                temp = wordchar[i]
                wordchar[i] = '*'
                wordexpand = ''.join(wordchar)
                addword(wordexpand)
                id2 = wordIDList[wordexpand]
                edge[id1].append(id2)
                edge[id2].append(id1)
                wordchar[i] =temp
        for word in wordList:
            addedg(word)
        addedg(beginWord)

        if endWord not in wordList:
            return 0

        nodeNum = len(wordIDList)
        beginwordID = wordIDList[beginWord]
        disBegin = [float("inf")] * nodeNum
        disBegin[beginwordID] = 0
        begindeque = collections.deque()
        begindeque.append(beginwordID)

        endwordID = wordIDList[endWord]
        disend = [float("inf")] * nodeNum
        disend[endwordID] = 0
        enddeque = collections.deque()
        enddeque.append(endwordID)
        while begindeque or enddeque:
            queBeginSize = len( begindeque)
            for _ in range(queBeginSize):
                nodeBegin = begindeque.popleft()
                if disend[nodeBegin] != float("inf"):
                    return (disBegin[nodeBegin] + disend[nodeBegin]) // 2 + 1
                for it in edge[nodeBegin]:
                    if disBegin[it] == float("inf"):
                        disBegin[it] = disBegin[nodeBegin] + 1
                        begindeque.append(it)

            queBeginSize = len(enddeque)
            for _ in range(queBeginSize):
                nodeend =  enddeque.popleft()
                if disBegin[nodeend] != float("inf"):
                    return (disBegin[nodeBegin] + disend[nodeBegin]) // 2 + 1
                for it in edge[nodeend]:
                    if disend[it] == float("inf"):
                        disend[it] = disend[nodeend] + 1
                        enddeque.append(it)
        return 0