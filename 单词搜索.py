from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        global wordVisted,Visted
        wordPath = ''
        wordVisted=[]
        wordFind=word
        m=len(board)
        n= 0
        dir = [[1,0],[0,1],[-1,0],[0,-1]]
        if m>0:
            n = len(board[0])
        Visted = [[0 for _ in range(n)] for _ in range(m)]
        def wordFindStr(x,y,wordPath,wordFind,word):
            global wordVisted, Visted
            if len(wordFind) ==0 :
                return True
            for i in dir:
                j = x+i[0]
                k = y+i[1]
                if  j>=0 and j<m and k>=0 and k<n and board[j][k]==wordFind[0]:
                    if len(wordPath)==m*n-1:
                        continue
                    if Visted[j][k]==1:
                        continue
                    # wordPath = wordPath+board[j][k]
                    Visted[j][k]=1
                    start = [j,k]
                    if wordFindStr(j,k,wordPath+board[j][k],wordFind[1:],word)==True:
                        return True
                    else:
                        Visted[j][k]=0
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    wordFind=word[1:]
                    Visted[i][j] = 1
                    if wordFindStr(i,j,wordPath,wordFind,word) == True:
                        return True
                    else:
                        Visted[i][j] = 0
        return False
