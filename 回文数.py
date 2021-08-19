class Solution:
    def isPalindrome(self, x: int) -> bool:
        int_s = str(x)
        if len(int_s)<2:
            return True
        if len(int_s)==2:
            if int_s[0]==int_s[-1]:
                return True
            else:
                return False
        if int_s[0]==int_s[-1] and self.isPalindrome(int_s[1:-1]) is True:
            return True
        else:
            return False