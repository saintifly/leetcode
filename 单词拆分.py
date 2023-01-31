class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        global wordPath,words,visted
        wordPath = []
        words = s
        visted=[]
        def wordFind(wordDict):
            global wordPath,words,visted
            if s == ''.join(wordPath) :
                return True
            for word in wordDict:
                if word in words and ''.join(wordPath)+word not in visted:
                    wordlen = len(word)
                    if words[:wordlen]==word:
                        words = words[wordlen:]
                        wordPath.append(word)
                        if ''.join(wordPath) not in visted:
                            visted.append(''.join(wordPath))
                        if wordFind(wordDict)==True:
                            return True
                        words = wordPath[-1]+words
                        wordPath = wordPath[:-1]
            return False
        return wordFind(wordDict)