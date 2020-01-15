class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        c =  '{:b}'.format(x^y)
        count = 0
        for i in c:
            if i=="1":
                count =count +1
        return count 