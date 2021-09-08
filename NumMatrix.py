import numpy as np
import copy
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrixcopy = matrix
        self.matrix = copy.deepcopy(self.matrixcopy)
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        rownum = len(self.matrix )
        pre=0
        
        for i,row_item in enumerate(self.matrix):
            for j,col_item in enumerate(row_item):
                self.matrix[i][j] = self.matrix[i][j] + pre
                pre = self.matrix[i][j]
            pre = 0
            if i>0:
                self.matrix[i] = list(np.array(self.matrix[i])+np.array(self.matrix[i-1]))
        if col1-1<0 and row1-1<0:
            ret  = int(self.matrix[row2][col2] - 0)
        elif col1-1<0:        
            ret  = int(self.matrix[row2][col2] - self.matrix[row1-1][col2])
        elif row1-1<0:
            ret  = int(self.matrix[row2][col2] - self.matrix[row2][col1-1])
        else:
            ret = int(self.matrix[row2][col2] - self.matrix[row1-1][col2] -self.matrix[row2][col1-1] + self.matrix[row1-1][col1-1])
        if (row1 ==  row2 and col1 == col2):
            self.matrix = copy.deepcopy(self.matrixcopy)
            return self.matrixcopy[row1][col1]
        if len(self.matrix) ==1 or len(self.matrix[0]) ==1:
            if row1-1<0 or col1-1<0:
                pre = 0
            else:
                pre = self.matrix[row1-1][col1-1]
            ret  = int(self.matrix[row2][col2] - pre)
        
        self.matrix = copy.deepcopy(self.matrixcopy)
        return ret 