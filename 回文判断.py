class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temps=''
        for char_c in s:
            if char_c.isdigit():
                temps=temps+char_c
            if char_c.isalpha():
                temps=temps+char_c.lower()
        len_tmp = len(temps);
        for i in range(len_tmp):
            if temps[i]!=temps[-i-1]:
                return False
        return True
