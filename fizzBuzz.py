class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        out_ret = []
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                out_ret.append("FizzBuzz")
            elif i%3==0:
                out_ret.append("Fizz")
            elif i%5==0:
                out_ret.append("Buzz")
            else:
                out_ret.append(str(i))      
        return out_ret