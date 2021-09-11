class Solution:
    def isPalindrome(self, s: str) -> bool:
        sLen = len(s)
        left = 0
        right = sLen-1
        while(left<right):
            while (s[left].isalnum() is not True and left<right):
                left= left+1
            while(s[right].isalnum() is not True and left< right):
                right -=1
            if s[left].lower()==s[right].lower():
                left +=1
                right -=1
                continue
            else:
                print(s[left],s[right])
                return False
        return True