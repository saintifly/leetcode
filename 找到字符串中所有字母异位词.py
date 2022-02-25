class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        snum = len(s)
        pnum = len(p)
        if pnum>snum:
            return []
        sList = [0]*26
        pList = [0]*26
        ret = []
        for i in range(len(p)):
            pList[ord(p[i])-ord('a')] +=1
            sList[ord(s[i])-ord('a')] +=1
        if pList == sList:
            ret.append(0)
        for i in range(len(s)-len(p)):
            sList[ord(s[i])-ord('a')] -=1
            sList[ord(s[i+len(p)])-ord('a')] +=1
            if pList==sList:
                ret.append(i+1)
        return ret