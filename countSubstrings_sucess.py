class Solution:
    def countSubstrings(self, s: str) -> int:
        sNum =len(s)
        ret1 = []
        for i in range(2*sNum-1):
            left = i//2
            right = i//2+i%2
            print(left,right)
            while(left>=0 and right<sNum and s[left]==s[right]):
                ret1.append([left,right])
                left = left -1
                right = right +1
        print(ret1)
        return len(ret1)