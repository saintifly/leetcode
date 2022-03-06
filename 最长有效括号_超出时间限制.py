class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        '('£¬')'£¬'{'£¬'}'£¬'['£¬']'
        """
        while True:
            if ' ' in s:
                s.remove(' ')
            else:
                break
        if len(s)%2 !=0:
            return False
        little_tmp = []
        for i in range(len(s)):
            if s[i] =="(":
                little_tmp.append("(")
            if s[i] ==")":
                if little_tmp ==[]:
                    return False
                while little_tmp !=[] and little_tmp[-1] !="(":
                    little_tmp.pop(-1)
                if little_tmp !=[]:
                    little_tmp.pop(-1)
                else:
                    return False
        if little_tmp==[]:
            return True
        else:
            return False

    def longestValidParentheses(self, s: str) -> int:
        sLen  = len(s)
        sMaxLen  = 0
        sSqunen = deque()
        sSqunen.append(s)
        while(len(sSqunen)!=0):
            s1 = sSqunen.popleft()
            if self.isValid(s1):
                sMaxLen = len(s1)
                break
            if s1[:-1] not in sSqunen:
                sSqunen.append(s1[:-1])
            if s1[1:] not in sSqunen:
                sSqunen.append(s1[1:])
        return sMaxLen
            

