import os
import math

def is_the_squeen_card(input_list=[]):
    '''
    :param input_list: 输出列表，1-13，大王为0，小王为0
    :return:
    '''
    if len(input_list) != 5:
        return -1
    if 0 not in input_list:
        input_list_set = set(input_list)
        if len(input_list) != len(input_list_set):
            return False
    input_list = sorted(input_list)
    zero_count = 0
    diff_num = 0
    for i,input_iterm in enumerate(input_list):
        if input_iterm == 0:
            zero_count = zero_count + 1
            input_list.remove(0)
        else:
            if i>0:
                if input_iterm-input_list[i-1]==0:
                    return False
                diff_num = diff_num+input_iterm-input_list[i-1]
    if diff_num < zero_count +len(input_list):
        return True
    else:
        return False



if __name__ == '__main__':
    ret = is_the_squeen_card([5,1,2,0,3])
    print(ret)
