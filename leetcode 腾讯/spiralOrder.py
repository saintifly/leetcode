class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = 0
        n = 0
        ret_List = []
        
        while True:
            m = len(matrix)
            if m == 0:
                break
            n = len(matrix[0])
            if n ==0:
                break
            for i in range(n):
                ret_List.append(matrix[0][i])
            matrix.remove(matrix[0])
            if m ==1:
                break
            for i in range(m-2):
                ret_List.append(matrix[i][n-1])
                matrix[i].pop()
            for i in range(n,0,-1):
                ret_List.append(matrix[-1][i-1])
            matrix.remove(matrix[-1])
            if n == 1:
                break
            for i in range(m-2,0,-1):
                ret_List.append(matrix[i-1][0])
                matrix[i-1].pop(0)
        return ret_List