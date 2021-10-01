class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = []
        temp = 1
        for i,item in enumerate(temperatures):
            flag = 0
            for j in temperatures[i+1:]:
                if j<=item:
                    temp +=1
                else:
                    flag = 1
                    out.append(temp)
                    temp = 1
                    break
            if flag == 0:
                out.append(0)
                temp = 1 
                flag = 0   
        return out