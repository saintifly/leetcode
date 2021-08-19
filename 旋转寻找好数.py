class Solution:
    def rotatedDigits(self, n: int) -> int:
        lenOfn = len(str(n))
        res = []
        for i in range(1, n + 1):
            flag = 1
            str_of_i = list(str(i))
            for k, j in enumerate(str_of_i):
                if j in ['0', '1', '8']:
                    continue
                if j in ['3', '4', '7']:
                    flag = 0
                    break
                if j == '2':
                    str_of_i[k] = '5'
                if j == '5':
                    str_of_i[k] = '2'
                if j == '6':
                    str_of_i[k] = '9'
                if j == '9':
                    str_of_i[k] = '6'
            str_of_i_1 = "".join(str_of_i)
            if int(str_of_i_1) != i and flag ==1:
                res.append(i)
        return len(res)