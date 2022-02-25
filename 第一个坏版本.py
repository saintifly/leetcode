# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n, n_min=1):
        """
        :type n: int
        :rtype: int
        """
        n_half = (n-n_min)
        if n_half == 0 :
            return n_min
        if n-n_min == 1:
            if isBadVersion(n) is True and  isBadVersion(n_min) is False:
                return n
        n_half = n_half/2 + n_min
        if isBadVersion(n_half) is True:  
            return self.firstBadVersion(n_half, n_min)
        else:
            return self.firstBadVersion(n, n_half)