class Solution:
    def maxRectangLine(self,rectang:List[int])->int:
        a=[]
        a.append(-1)
        rectang.append(0)
        tmp  = 0 
        out = 0
        for i,item in enumerate(rectang):
            if item > rectang[a[-1]]:
                tmp = i
                a.append(i)
            else:
                while(item <= rectang[a[-1]] and a!=[-1]):
                    c = a.pop()
                    out = max(rectang[c]*(i-a[-1]-1),out)
                a.append(i)
        return out

    def maximalRectangle(self, matrix: List[str]) -> int:
        ##
        # a=[]
        # out = 0
        # for i,item in enumerate(matrix):
        #     item = list(map(int, item))
        #     a.append(item)
        #     if i>0:
        #         a[i] = [j*(j + k) for j, k in zip(a[i], a[i-1])]
        #     print(a)
        #     tmp =  self.maxRectangLine(a[i])
        #     out =  max(out,tmp)
        # return out
        Row = len(matrix)
        if Row == 0:
            return 0
        Col = len(matrix[0])

        res = 0
        heights = [0 for _ in range(Col)]
        for r in range(Row):
            for c in range(Col):
                if matrix[r][c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0
            res = max(res, self.maxRectangLine(heights))
        return res