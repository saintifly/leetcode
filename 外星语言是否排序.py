class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i,item in enumerate(words):
            if i==0:
                continue
            for j,item1 in enumerate(item):
                if j< len(words[i-1]):
                    if order.index(item1) < order.index(words[i-1][j]):
                        return False
                    if order.index(item1) > order.index(words[i-1][j]):
                        break
            if len(words[i-1])>len(item):
                if item1== item[-1] and  order.index(item1) == order.index(words[i-1][j]):
                        return False
        return True

