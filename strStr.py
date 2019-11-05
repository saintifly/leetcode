class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        if needle not in haystack:
            return -1
        len_dst = len(needle)
        temp = 0
        count = 0
        for i,char_src in enumerate(haystack):
            if haystack[i:i+len_dst]==needle:
                return i