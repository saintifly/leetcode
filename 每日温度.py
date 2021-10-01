class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0]*len(temperatures)
        stack  = []
        for i,item in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<item:
                index = stack.pop()
                ret[index] = i - index
            stack.append(i)
        return ret 