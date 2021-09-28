class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1Num = len(s)
        s2Num = len(t)
        if s1Num != s2Num:
            return False
        if s == t:
            return False
        s1List = [0]*26
        s2List = [0]*26
        for i in range(len(s)):
            s1List[ord(s[i])-ord('a')] +=1
            s2List[ord(t[i])-ord('a')] +=1
        if s1List== s2List:
            return True
        else:
            return False