class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        retsult_list =[]
        for i in range(20):
            for j in range(20):
                ret = x**i +y**j
                if  ret <= bound:
                    retsult_list.append(ret)
        return list(set(retsult_list))