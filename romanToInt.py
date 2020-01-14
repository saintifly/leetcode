class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        unit_list = {"I":1, "V":5,"X":10,"L":50, "C":100, "D":500, "M":1000, "4":4, "9":9,"A":40,"B":90,"E":400,"F":900}
        List_val = []
        for s_unit in s:
            List_val.append(unit_list[s_unit])
        #List_val.sort(reverse=False)
        n = len(List_val)
        flag=0
        print List_val
        for i in range(n-1):
            if List_val[i] < List_val[i+1]:
                flag = 1
        if flag == 0:
            ret = 0 
            for i in range(n):
                ret = ret + List_val[i]
            return ret
        if flag == 1:
            if "IV" in s:
                s=s.replace("IV","4")
            if "IX" in s:
                s=s.replace("IX","9")
            if "XL" in s:
                s=s.replace("XL","A")
            if "XC" in s:
                s=s.replace("XC","B")                
            if "CD" in s:
                s=s.replace("CD","E")
            if "CM" in s:
                s=s.replace("CM","F")  
        ret = 0
        n=len(s)
        for i in range(n):
                ret = ret + unit_list[s[i]]
        return ret