class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        import numpy as np
        s1List = [0]*26
        strsToOrd = []
        for i in strs:
            for j in i:
                s1List[ord(j)-ord('a')] +=1
            print(s1List)
            s1List = [str(x) for x in s1List]
            s2= 'a'.join(s1List)
            strsToOrd.append(s2)
            s1List = [0]*26
        outlist = []
        tmp =[]
        strsToOrdSet = set(strsToOrd)
        npList =  np.array(strsToOrd)
        for i in strsToOrdSet:
            eq_letter = np.where(npList == i)
            for i in eq_letter[0]:
                tmp.append(strs[i])
            outlist.append(tmp)
            tmp=[]
        return outlist


# #将列表转换为numpy的数组
# a = np.array(["a","b","c","a","d","a"])
# #获取元素的下标位置
# eq_letter = np.where(a == "a")
# print(eq_letter[0])#[0 3 5]
