class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        num = len(strs)
        flag = 0;
        if num == 0:
            return ""
        if num ==1:
            return strs[0]
        min_len = len(strs[0])
        str_min = strs[0]
        ret_num  = 0
        for strs_tmp in strs:
            len_tmp = len(strs_tmp)
            if len_tmp < min_len:
                min_len = len_tmp
                str_min = strs_tmp
        if min_len==0:
            return ""    
        for i in range(min_len+1):
            for strs_tmp in strs:
                if len(strs_tmp)==1 or i==0:
                    if strs_tmp[0] != str_min[0]:
                        flag = 1
                        break;   
                elif strs_tmp[0:i] != str_min[0:i]:
                    flag = 1
                    break;
            if i==0 and flag ==1:
               return ""
            if i==1 and flag ==1:
               return strs_tmp[0]
            if len(strs_tmp[0:i-1])>0 and flag ==1:
                return strs_tmp[0:i-1]
        if flag==1:
            return ""
        if flag ==0:
            return str_min
            
    
       
        
            