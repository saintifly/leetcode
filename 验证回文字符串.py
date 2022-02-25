class Solution:
    def validPalindrome1(self, s: str) -> bool:
        sLen = len(s)
        left = 0
        right = sLen-1
        ret = 0
        while(left<right):
            print(s[left],s[right])
            if ret >1:
                return False
            if s[left]==s[right]:
                left +=1
                right -=1
                continue
            if s[left+1]==s[right]:
                ret = ret+1
                left +=1
                continue
            if  s[left]==s[right-1]:
                ret = ret+1
                right -=1
                continue
            return False
        if ret >1:
            return False
        return True

    def validPalindrome(self, s: str) -> bool:
        if self.validPalindrome1(s) is True:
            return True
        sLen = len(s)
        left = 0
        right = sLen-1
        ret = 0
        print(sLen)
        while(left<right):
            if ret >1:
                return False
            if s[left]==s[right]:
                left +=1
                right -=1
                continue
            if  s[left]==s[right-1]:
                ret = ret+1
                right -=1
                continue
            if s[left+1]==s[right]:
                ret = ret+1
                left +=1
                continue
            return False
        if ret >1:
            return False
        return True

