class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        wordList = sentence.split(" ")
        dictionary.sort(key = lambda i:len(i),reverse=True)
        for j,word in enumerate(wordList):
            for i in dictionary:
                if word.startswith(i) ==True:
                    wordList[j] = i
        sentence = " ".join(wordList)
        return sentence