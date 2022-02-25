class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        print n
        a =  '{:b}'.format(n)
        b = '0b'+a[::-1]+"0"*(32-len(a))
        c = int(b,2)
        return c 
        