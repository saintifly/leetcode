class Solution:
    def countBits(self, n: int) -> List[int]:
        retsutl=[]
        for i in range(n+1):
            bin_i = bin(i)
            count = 0
            for i in bin_i:
                if i=='1':
                    count = count +1
            retsutl.append(count)
        return retsutl