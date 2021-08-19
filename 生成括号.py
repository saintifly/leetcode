class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        if n == 1:
            return ['()']
        res = []
        res.append([])
        res.append(['()'])
        res_n =[]
        for i in range(2,n+1):
            for item in res[i-1]:
                for j in range((i-1)*2):
                    res_tmp = '('+item[:j]+')'+item[j:]
                    res_n.append(str(res_tmp))
            res.append(list(set(res_n)))
            res_n=[]
        return res[-1]
