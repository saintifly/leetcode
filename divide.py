class Solution:
    import math
    def divide(self, a: int, b: int) -> int:
       if a//b >2**31-1 or a//b<-2**31:
           return 2**31-1
       if a//b<0 and math.fmod(a,b)!=0:
           return a//b+1 
       return a//b