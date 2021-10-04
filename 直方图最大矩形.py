class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ##实现单调递增栈
        a=[]
        a.append(-1)
        heights.append(0)
        tmp  = 0 
        out = 0
        for i,item in enumerate(heights):
            if item > heights[a[-1]]:
                tmp = i
                a.append(i)
            else:
                while(item <= heights[a[-1]] and a!=[-1]):
                    c = a.pop()
                    out = max(heights[c]*(i-a[-1]-1),out)
                a.append(i)
        return out