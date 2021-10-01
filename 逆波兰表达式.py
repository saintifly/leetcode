class Solution:
    def is_number(self,str):
        try:
            # 因为使用float有一个例外是'NaN'
            if str=='NaN':
                return False
            float(str)
            return True
        except ValueError:
            return False
    def evalRPN(self, tokens: List[str]) -> int:
        a=[]
        if len(tokens)==1:
            return int(tokens[0])
        for i in tokens:
            if self.is_number(i):
                a.append(i)
            else:
                tmp_1 = a.pop()
                tmp_exp = (str(a.pop())) + i + (str(tmp_1))
                tmp = int(eval(tmp_exp))
                a.append(tmp)
        if len(a)>1:
            return 0
        return a[0]