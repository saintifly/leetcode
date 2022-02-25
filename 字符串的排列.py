class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1Num = len(s1)
        s2Num = len(s2)
        if s1Num> s2Num:
            return False
        s1List = [0]*26
        s2List = [0]*26
        for i in range(len(s1)):
            s1List[ord(s1[i])-ord('a')] +=1
            s2List[ord(s2[i])-ord('a')] +=1
        if s1List== s2List:
            return True
        for i in range(len(s2)-len(s1)):
            s2List[ord(s2[i])-ord('a')] -=1
            s2List[ord(s2[i+len(s1)])-ord('a')] +=1
            if s1List== s2List:
                return True
        return False