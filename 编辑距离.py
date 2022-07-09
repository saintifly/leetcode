
from typing import List
def minDistance( word1: str, word2: str) -> int:
    m = len(word1)
    n = len(word2)
    mDistant = [[0 for i in range(n+1)] for j in range(m+1)]
    mDistant[0][0]= 0
    for i in range(1,m+1):
        mDistant[i][0] = mDistant[i-1][0]+1
    for j in range(1,n+1):
        mDistant[0][j] = mDistant[0][j-1] + 1
    for i in range(1,m+1):
        for j in range(1,n+1):
            if word1[i-1] == word2[j-1]:
                mDistant[i][j] = mDistant[i-1][j-1]
            else:
                 mDistant[i][j] = min(mDistant[i][j-1],mDistant[i-1][j],mDistant[i-1][j-1])+1
    return mDistant[-1][-1]

if __name__ == '__main__':
    word1 = 'horse'
    word2 = 'ros'
    out = minDistance(word1,word2)
    print(out)