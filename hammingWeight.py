class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        a =  '{:b}'.format(n)
        count = 0
        for i in a:
            if i=="1":
                count =count +1
        return count 