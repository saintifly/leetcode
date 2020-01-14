class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        import math
        count = 0
        if n<3:
            return 0
        for i in range(1, n,2):
            for j in range(1, int(math.sqrt(i))):
                if i%(j+1) == 0:
                    break
            else:
                count = count +1
       
        return count
        """
        """
        if n<3:
            return 0
        if n==3:
            return 1
        count = 1
        for i in range(2, n):
            if n==3 or n==2:
                count = count +1
            if i%6!=1 and i%6!=5:
                continue
            for j in range(5, int(math.sqrt(i)),6):
                if i%j==0 or i%(j+2)==0:
                    continue
            else:
                print i
                count = count +1
        return count 
        ################https://blog.csdn.net/songyunli1111/article/details/78690447
    """
        if n < 3:
            return 0
        primes = [1] * n   # 广播
        primes[0] = primes[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [0] * len(primes[i * i: n: i])  # i*i到n之间隔i取一次数
        return sum(primes)