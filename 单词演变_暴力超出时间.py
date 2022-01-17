class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
            Wordn = len(beginWord)
            wordm = len(wordList)
            ret = 1
            currentword = [beginWord]
            while True:
                nextWordList = []
                for i in currentword:
                    for j in wordList:
                        if i == j:
                            continue
                        for k in range(Wordn):
                            if i[:k] == j[:k] and i[k+1:] == j[k+1:]:
                                if j == endWord:
                                    return ret+1
                                else:
                                    nextWordList.append(j)
                currentword = nextWordList
                ret = ret +1
                if ret >= wordm:
                    return 0