class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        count = 1
        num = 0 
        ret = "1"
        ret1 = ""
        if n ==1 or n=="1":
            return "1"
        for i in range(n-1):
            num = len(ret)
            for j,num_part in enumerate(ret):
                if  j<num-1 and  num_part == ret[j+1]:
                    count =  count + 1
                    continue
                if count > 1:
                    ret1 = ret1+ str(count)+num_part
                    count = 1
                else:
                    ret1 = ret1+"1"+num_part
            ret =ret1
            ret1=""
            count = 1
        
        return ret