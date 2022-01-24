class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        wordIDList = dict()
        equationsEdge = collections.defaultdict(list)
        quationsvalue = collections.defaultdict(list)
        NodeID = 0

        def addword(word: str):
            nonlocal NodeID
            if word not in wordIDList:
                wordIDList[word] = NodeID
                NodeID = NodeID + 1

        def addedg(word: List[str], i: int):
            addword(word[0])
            addword(word[1])

            id1 = wordIDList[word[0]]
            id2 = wordIDList[word[1]]
            equationsEdge[id1].append(id2)
            equationsEdge[id2].append(id1)
            quationsvalue[id1].append(values[i])
            quationsvalue[id2].append(1/values[i])

        for i, word in enumerate(equations):
            addedg(word, i)
        ret = []

        '''wordIDList,equationsEdge,quationsvalue'''
        for item in queries:
            if item[0] not in wordIDList.keys() or item[1] not in wordIDList.keys():
                ret.append(-1)
                continue
            beginID = wordIDList[item[0]]
            endID = wordIDList[item[1]]
            if beginID==endID:
                ret.append(1)
                continue
            begindeque = collections.deque()
            begindevalue = collections.deque()
            begindeque.append([beginID])
            begindevalue.append([1])
            count = 0
            maxlen = len(wordIDList)
            retout = 1
            tmp =[]
            temp = []
            flag = 0
            while begindeque and count<maxlen+30:
                currentNode = begindeque.popleft()
                temp = begindevalue.popleft()
                for i,item in enumerate(currentNode):
                    if item == endID:
                        ret.append(temp[i])
                        flag = 1
                        break
                    else:
                        begindeque.append(equationsEdge[item])
                        for j,item1 in enumerate(equationsEdge[item]):
                            tmp.append(temp[i]*quationsvalue[item][j])
                        begindevalue.append(tmp)
                        tmp=[]
                        count = count+1
                if flag==1:
                    break
            else:
                ret.append(-1)
        return ret