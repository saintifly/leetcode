class Solution:
    def maxProduct(self, words: List[str]) -> int:
            mark = 0
            markintList = []
            for i in words:
                for j in i:
                    charj = ord(j) - ord('a')
                    mark |=1<<charj
                markintList.append(mark)
                mark = 0
            max_ret = 0
            for i in range(len(words)):
                for j in range(len(words)):
                    if markintList[i] & markintList[j] == 0:
                        mark_temp = len(words[i]) * len(words[j])
                        if int(mark_temp) > int(max_ret):
                            max_ret = mark_temp
            return max_ret