class Solution(object):
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
            if s[i] =="[":
                little_tmp.append("[")
            if s[i] =="]":
                if little_tmp ==[]:
                    return False
                while little_tmp !=[] and little_tmp[-1] !="[":
                    little_tmp.pop(-1)
                if little_tmp !=[]:
                    little_tmp.pop(-1)
                else:
                    return False
            if s[i] =="{":
                little_tmp.append("{")
            if s[i] =="}":
                if little_tmp ==[]:
                    return False
                while little_tmp !=[] and little_tmp[-1] !="{":
                    little_tmp.pop(-1)
                if little_tmp !=[]:
                    little_tmp.pop(-1)
                else:
                    return False
        if little_tmp==[]:
            return True
        else:
            return False