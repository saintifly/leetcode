class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        MaxStrSequeen = []
        maxlen = 0
        for i in s:
            if MaxStrSequeen==[] or i not in MaxStrSequeen:
                MaxStrSequeen.append(i)
                if len(MaxStrSequeen)>maxlen:
                    maxlen = len(MaxStrSequeen)
            elif MaxStrSequeen[0]==i:
                MaxStrSequeen.pop(0)
                MaxStrSequeen.append(i)
                continue
            else:
                while MaxStrSequeen[0]!=i:
                    MaxStrSequeen.pop(0)
                MaxStrSequeen.pop(0)
                MaxStrSequeen.append(i)
                continue
        return maxlen