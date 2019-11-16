 
        '''
        strs = ["dog","racecar","car"]
        num = len(strs)
        len_tmp = 0
        if num == 0:
            return ""
        min_len = len(strs[0])
        str_min = strs[0]
        ret_num  = 0
        for strs_tmp in strs:
            len_tmp = len(strs_tmp)
            if len_tmp < min_len:
                min_len = len_tmp
                str_min = strs_tmp
        for i in range(min_len):
            for strs_tmp in strs:
                print str_min[0:i]
                print strs_tmp[0:i]
                if str_min[0:i] != strs_tmp[0:i]:
                    
                    ret_num = i-1
                    print '11111'+str(i-1)
                    break
            print '22222'+str(ret_num)
            if ret_num != 0:
                break
        print ret_num
        if ret_num<0:
            return "" 
        print str_min[0:ret_num]
        return str_min[0:ret_num]
        '''