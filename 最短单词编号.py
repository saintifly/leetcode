class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        ret =''
        words = list(set(words))
        for i,item in enumerate(words):
            if item+'#' not in '#'.join(words[:i]+words[i+1:])+'#':
                ret = ret + item+'#'
        return len(ret)