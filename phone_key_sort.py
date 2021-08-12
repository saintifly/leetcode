import os
'''
实现
    put("2", "abc");
    put("3", "def");
    put("4", "ghi");
    put("5", "jkl");
    put("6", "mno");
    put("7", "pqrs");
    put("8", "tuv");
    put("9", "wxyz");
    给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
    给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
'''
import math
phone_num_map_str = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno",\
                     "7":"pqrs","8":"tuv","9":"wxyz"}
result_list=[]
return_tmp = ''
num = 1
def sort_phone_num_str(input_nums):
    """
    :param input_nums:
    :return:
    """
    global return_tmp
    global num
    if num == 1:
        for i in input_nums:
            if str(i) =="7" or str(i) =='9':
                num = 4*num
            else:
                num = 3*num
    if len(input_nums) == 1:
        for i in phone_num_map_str[input_nums]:
            result_list.append(return_tmp+str(i))
        return_tmp = ''
        return ''
    first_input_num = input_nums[0]
    for i in phone_num_map_str[first_input_num]:
        return_tmp = return_tmp + str(i)
        return_tmp = return_tmp + str((sort_phone_num_str(str(input_nums[1:]))))
        return_tmp = return_tmp[:-1]
    return_tmp = return_tmp[:-1]
    if len( result_list) ==num:
        return result_list
    return ''

if __name__ == '__main__':
    ret = sort_phone_num_str("222227")
    print(ret)